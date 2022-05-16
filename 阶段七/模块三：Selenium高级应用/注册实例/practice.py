from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

# 第一题
'''
1. 点击 alert按钮 
2.获取alert提示文本信息 
3.处理对话框同意/取消 

'''
driver = webdriver.Chrome()
web_path = 'file://' + os.path.dirname(os.path.abspath(__file__)) + '/注册实例.html'
driver.get(web_path)
driver.find_element(By.ID,"ZCA").click()
handles = driver.window_handles
driver.switch_to.window(handles[-1])

driver.find_element(By.ID,"alerta").click()
alert_text = driver.switch_to.alert.text
print(alert_text)
driver.switch_to.alert.accept()

# 第二题
# 移动到注册按钮上 预期：按钮变色 
action =ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"[type='submitA']")).perform()
time.sleep(1)
driver.get_screenshot_as_file(
    os.path.dirname(os.path.abspath(__file__)) +'/{}.png'.format(time.strftime('%Y%m%d-%H%M%S'))
    )


# 第三题
'''
1. 打开注册实例.html 
2. 填写主页面 页面信息 
3. 填写注册A 页面信息 
4、切换到默认目录 driver.switch_to.default_content() 
5. 填写注册B 页面信息
'''
driver.switch_to.window(handles[0])

driver.find_element(By.ID,'user').send_keys('admin')
driver.find_element(By.ID,'password').send_keys('123456')
driver.find_element(By.ID,'tel').send_keys('18600000000')
driver.find_element(By.ID,'email').send_keys('123@qq.com')

els = driver.find_elements(By.TAG_NAME,'iframe')
driver.switch_to.frame(els[0])
driver.find_element(By.ID,'userA').send_keys('admin')
driver.find_element(By.ID,'passwordA').send_keys('123456')
driver.find_element(By.ID,'telA').send_keys('18600000000')
driver.find_element(By.ID,'emailA').send_keys('123@qq.com')

driver.switch_to.default_content()

driver.switch_to.frame(els[1])
driver.find_element(By.ID,'userB').send_keys('admin')
driver.find_element(By.ID,'passwordB').send_keys('123456')
driver.find_element(By.ID,'telB').send_keys('18600000000')
driver.find_element(By.ID,'emailB').send_keys('123@qq.com')

driver.quit()