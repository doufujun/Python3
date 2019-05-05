#交互动作
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
src = browser.find_element_by_css_selector('#draggable')
tgt = browser.find_element_by_css_selector('#droppable')
action = ActionChains(browser)
action.drag_and_drop(src, tgt)
action.perform()