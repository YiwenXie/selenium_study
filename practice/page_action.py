import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'G:\geckodriver-v0.26.0-win64\geckodriver.exe')
browser.implicitly_wait(6)

url = 'https://www.baidu.com'

try:
    browser.get(url)
    time.sleep(2)
    browser.refresh()   # 刷新方法 refresh
    print('test pass: refresh successful')
    print(browser.capabilities['browserVersion'])  # 打印浏览器version的值
    elem_news = browser.find_element_by_link_text("新闻")
    elem_news.click()  # 点击进入到百度新闻
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    print(browser.current_url)  # current_url 方法可以得到当前页面的URL
    print(browser.title)  # title方法可以获取当前页面的标题显示的字段
    time.sleep(2)
    # browser.back()  # 从百度新闻后退到百度首页
    # time.sleep(2)
    # browser.forward()  # 百度首页前进到百度新闻
    # time.sleep(2)
    # ele = browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  # 触发ctrl + t 此条无用
    js = 'window.open("{}");'.format(browser.current_url)  # javaScript语句,通过这条语句在新的标签页再打开新的当前url
    browser.execute_script(js)  # 执行JavaScript语句
    print("success to add a new tab")
    time.sleep(1)
except Exception as e:
    print("element id is not be found", e)
finally:
    browser.quit()