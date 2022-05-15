import logging
import time
from selenium import webdriver
chrome_browser = None
base_url = 'http://150.158.25.85/index.php'

def get_css_path(value, attr='id',layer=None):
    '''
    layer:(parent_layer,current_layer)
    '''
    if layer is not None and layer != ():
        return f'{layer[0]}[{attr}={value}] > {layer[1]}'
    return f'[{attr}={value}]'


class BaseController:
    browser = None
    def __init__(self,file_path=None) -> None:
        global chrome_browser
        if chrome_browser is None:
            chrome_browser = webdriver.Chrome()

        self.browser = chrome_browser
        if file_path:
                self.reach_the_page(file_path)
                self.set_window_size()

    def get_browser(self):
        return self.browser
        
    def reach_the_page(self, file_path):
        self.browser.get(file_path)

    def close_the_page(self):
        self.browser.close()

    def scroll_into_view(self,element):
        element.location

    def set_window_size(self,width=None,height=None):
        if width is None and height is None:
            self.browser.maximize_window()
        else:
            self.browser.set_window_size(width, height)
    

    def get_element(self, key, position=0):
        element, length = self.wait_until_element_exists(key)
        if length > 1:
            element = element[position]
        self.scroll_into_view(element)
        return element

    def input_content(self,element,words):
        element.clear()
        element.send_keys(words)
        return element

    def click_element(self,element):
        element.is_enabled()
        element.click()
        return element

    def wait_until_element_exists(self, path, delay_time=1, step=1):
        els = None
        lst = [i for i in range(0,delay_time+1, step)]
        while lst:
            els = self.browser.find_elements_by_css_selector(path)
            length = len(els)
            if length != 0:
                if length == 1:
                    els = els[0]
                return els, length
            
            time.sleep(time.sleep(lst.pop()))

        raise Exception('没有找到元素,path:' + path)
        
    def wait_until_element_enabled(self, element, delay_time=1, step=1):
        lst = [i for i in range(0,delay_time+1, step)]
        while lst:
            if element.is_enabled():
                return True
            
            time.sleep(time.sleep(lst.pop()))

        raise Exception('没有找到元素,' + element)

    def is_text_present(self, text, delay=1):
        time.sleep(delay)
        assert str(text) in self.browser.page_source


class LoginPage(BaseController):
    def __init__(self, file_path=None) -> None:
        super().__init__(file_path)
        self.USER_NAME_INPUT = get_css_path("username")
        self.PASSWORD_INPUT = get_css_path("password")
        self.VERIFY_CODE_INPUT = get_css_path("verify_code")
        self.SUBMIT_BTN = get_css_path("sbtbutton","name")

    def login(self,user_name,pwd):
        self.input_content(self.get_element(self.USER_NAME_INPUT),user_name)
        self.input_content(self.get_element(self.PASSWORD_INPUT),pwd)
        self.input_content(self.get_element(self.VERIFY_CODE_INPUT),'8888')
        self.click_element(self.get_element(self.SUBMIT_BTN))


class HomePage(BaseController):
    def __init__(self, file_path=None) -> None:
        super().__init__(file_path)
        self.GO_BACK_TO_HOME_BTN = get_css_path("home","class")
        self.SEARCH_INPUT = get_css_path("q")
        self.SEARCH_BTN = get_css_path("search_usercenter_btn", "class")
        self.COMMODITY_CARD = get_css_path("shop_name2", "class", ("div","a"))

    def search_commodity(self, words):
        self.input_content(self.get_element(self.SEARCH_INPUT), words)
        self.click_element(self.get_element(self.SEARCH_BTN))
        

    def go_to_the_first_commodity_detail(self):
        element = self.get_element(self.COMMODITY_CARD)
        commodity_text = element.text
        self.click_element(element)
        return commodity_text
            

class CommodityPage(BaseController):
    def __init__(self, file_path=None) -> None:
        super().__init__(file_path)
        self.BUY_NOW_BTN = get_css_path("buy_now")

    def buy_now(self):
        self.click_element(self.get_element(self.BUY_NOW_BTN))
        

class CartPage(BaseController):
    def __init__(self, file_path=None) -> None:
        super().__init__(file_path)
        self.USER_MONEY_CHECKBOX = get_css_path("user_money_checkbox")
        self.USER_MONEY_INPUT = get_css_path("user_money")
        self.PRICE_TEXT = get_css_path("payables")
        self.PAY_PWD_INPUT = get_css_path("pay_pwd")
        self.SUBMIT_ORDER_BTN = get_css_path("submit_order")

    def use_rest_money(self,price):
        checkbox = self.get_element(self.USER_MONEY_CHECKBOX)
        if checkbox.is_selected() is False:
            self.click_element(checkbox)
        if checkbox.is_selected():
            element = self.get_element(self.USER_MONEY_INPUT)
            self.input_content(element,price)

    def get_price_text(self):
        price_text = self.get_element(self.PRICE_TEXT).text
        price_text = ''.join([i for i in price_text[1:]])
        return price_text

    def submit_order_without_money(self, pwd):
        price_text = self.get_price_text()
        self.use_rest_money(price_text)
        time.sleep(1)

        self.input_content(self.get_element(self.PAY_PWD_INPUT), pwd)
        price_text = self.get_price_text()
        if price_text == "0":
            self.click_element(self.get_element(self.SUBMIT_ORDER_BTN))
        

class OrderPage(BaseController):
    def __init__(self, file_path=None) -> None:
        super().__init__(file_path)
        self.ORDER_NO_TEXT = get_css_path("ddn1","class",("p","span"))

    def get_order_number(self):
        return self.get_element(self.ORDER_NO_TEXT,-1).text


if __name__ == "__main__":
    pwd = '123456'
    login_page = LoginPage(base_url + '/Home/user/login.html')
    login_page.login('13800138006', pwd)
    login_page.is_text_present("返回商城首页")

    home_page = HomePage()
    home_page.search_commodity('手机')
    text = home_page.go_to_the_first_commodity_detail()
    home_page.is_text_present(text)

    commodity_page = CommodityPage()
    commodity_page.buy_now()
    commodity_page.is_text_present("填写并核对订单信息")

    cart_page = CartPage()
    cart_page.submit_order_without_money(pwd)
    time.sleep(5)

    order_page = OrderPage()
    print("订单号",order_page.get_order_number())
    order_page.close_the_page()