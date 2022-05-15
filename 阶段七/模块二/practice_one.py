from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


def get_element_by_css_attr(value, attr='id',layer=None):
    '''
    layer:(parent_layer,current_layer)
    '''
    if layer is not None and layer != ():
        return driver.find_element_by_css_selector(f'{layer[0]}[{attr}={value}] > {layer[1]}')
    return driver.find_element_by_css_selector('#')


try:
    driver = webdriver.Chrome()
    web_path = 'file://' + os.path.dirname(os.path.abspath(__file__)) + '/注册A.html'
    driver.get(web_path)

    driver.find_element_by_css_selector('#userA').send_keys('admin')
    driver.find_element_by_css_selector('#passwordA').send_keys('123456')
    driver.find_element_by_css_selector('#telA').send_keys('18600000000')
    driver.find_element_by_css_selector('#emailA').send_keys('123@qq.com')
    time.sleep(2)
    driver.find_element_by_css_selector('[type="submitA"]').click()
    time.sleep(3)
except Exception as e:
    print(e.args)
    
finally:
    driver.close()
