import time

from selenium import webdriver


browser = webdriver.Firefox(executable_path=r'G:\geckodriver-v0.26.0-win64\geckodriver.exe')
browser.implicitly_wait(6)

url = 'https://www.baidu.com'

try:
    browser.get(url)
    time.sleep(2)
    # string = browser.find_element_by_id('kw').is_displayed()
    # print("find element by id is enable", string)
    # browser.find_element_by_tag_name('form').is_selected()
    # print("find element by form is enable", string)
    # browser.find_element_by_link_text('新闻').is_enabled()
    # print("find element by link text is enable", string)
    # browser.find_element_by_partial_link_text('首页').click()
    # print("find element by partial link text is enable")
    # string = browser.find_element_by_class_name('s_ipt').is_enabled()
    # print("find element by class name is enable", string)
    # string = browser.find_element_by_name('wd').is_enabled()
    # print("find element by name is enable", string)
    string = browser.find_element_by_css_selector('#su').is_enabled()
    print("find element by name is enable", string)
except Exception as e:
    print("element id is not be found", e)
finally:
    browser.quit()
