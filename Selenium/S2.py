from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_css_selector('#q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
btn = browser.find_element_by_css_selector('.btn-search')
btn.click()
login_btn = browser.find_element_by_css_selector('#J_Quick2Static')
if login_btn:
    login_btn.click()
    username = browser.find_element_by_css_selector('#TPL_username_1')
    password = browser.find_element_by_css_selector('#TPL_password_1')
    username.send_keys('123123')
    password.send_keys('admin')
else:
    pass