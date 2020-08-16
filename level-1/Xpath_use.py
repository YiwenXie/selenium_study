import time

from selenium import webdriver


browser = webdriver.Firefox(executable_path=r'G:\geckodriver-v0.26.0-win64\geckodriver.exe')
# 隐式等待
browser.implicitly_wait(10)
url = 'https://www.baidu.com'
try:
    # 打开网页一个拖拽实例
    browser.get(url)
    input = browser.find_element_by_xpath("//input[@id='kw']")
    input.send_keys("华为")
    time.sleep(1)
    input.clear()
    input.send_keys('小米')
    button = browser.find_element_by_xpath("//input[@id='su']")
    button.click()
    time.sleep(2)
    string = browser.find_element_by_xpath("//a[contains(@class,'ec-official-site')]/../a//em").text
    # string = browser.find_element_by_xpath("//a[contains(@class,'ec-official-site')]/../a/em[text()='小米']").text
    # string = browser.find_element_by_xpath("//a[contains(@class,'ec-official-site')]").text
    # print(string)
    if (string == '小米'):
        print("测试成功，结果和预期结果匹配！")
finally:
    browser.close()


