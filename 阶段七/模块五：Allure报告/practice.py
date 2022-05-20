import logging
import time
from selenium import webdriver
import pytest
import allure
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

    @allure.step("输入用户名{user_name}")
    def input_user_name(self,user_name):
        self.input_content(self.get_element(self.USER_NAME_INPUT),user_name)

    @allure.step("输入密码{pwd}")  
    def input_password(self,pwd):
        self.input_content(self.get_element(self.PASSWORD_INPUT),pwd)

    @allure.step("输入验证码{code}")
    def input_verify_code(self,code):
        self.input_content(self.get_element(self.VERIFY_CODE_INPUT),code)

    @allure.step("点击登录")
    def click_login(self):
        self.click_element(self.get_element(self.SUBMIT_BTN))
    

@allure.feature("登录页面")
class Testlogin():
    def setup(self):
        self.login_page = LoginPage(base_url + '/Home/user/login.html')

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('登录成功')
    def test_login(self):
        self.login_page.input_user_name('13800138006')
        self.login_page.input_password('123456')
        self.login_page.input_verify_code('8888')
        self.login_page.click_login()
        self.login_page.is_text_present("返回商城首页")

    def teardown(self):
        self.login_page.close_the_page()


    
    

