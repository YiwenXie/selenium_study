import time

from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Firefox(executable_path=r'G:\geckodriver-v0.26.0-win64\geckodriver.exe')
browser.implicitly_wait(6)

url = 'https://www.runoob.com/html/html-forms.html'

try:
    browser.get(url)
    time.sleep(2)
    # ActionChains(browser).move_to_element().perform()
    for i in browser.find_elements_by_xpath("//*/input[@type='radio']"):    # 因为点击，所以能够自动将滚轮滑动至单选框位置
        i.click()
        time.sleep(3)   # 睡眠只是为了看选中效果
except Exception as e:
    print(e)
finally:
    browser.quit()
