from selenium import webdriver
import re
import time
import xlwt


wb = xlwt.Workbook()
ws = wb.add_sheet('E-mails')

browser = webdriver.Firefox(executable_path=r'G:\geckodriver-v0.26.0-win64\geckodriver.exe')
# 隐式等待
browser.implicitly_wait(10)
url = 'http://www.baidu.com/'
try:
    browser.get(url)
    browser.find_element_by_xpath("//*/a[text()='关于百度']").click()
    # browser.find_element_by_xpath("//*/a[contains(@href,'home')]")
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element_by_xpath("//*/a[contains(@href,'contact')]").click()
    browser.switch_to.window(browser.window_handles[2])
    # browser.find_element_by_xpath("//*//*/a[text()='联系我们']").click()
    # browser.find_element_by_xpath("//div[@class='bd-content-nav nav-show J-bd-nav']//*/a[contains(@href,'contact')]").click()
    # browser.find_element_by_xpath("//*/div[@class='bd-content-nav nav-show J-bd-nav']//*/a[text()='联系我们']").click()
    # browser.find_element_by_xpath("//div[@class='bd-content-nav nav-show J-bd-nav']//li[4]//a[1]").click()
    # browser.find_element_by_xpath("//*[@id='indexAdmin']/div[1]/div/div/div/div[2]/ul/li[4]/a").click()
    time.sleep(2)
    # print(browser.current_window_handle)
    # handles = browser.window_handles
    # print(handles)
    # for handle in handles:
    #     if handle != browser.current_window_handle:
    #         # browser.close()
    #         print("马上切换到新标签页", handle)
    #         browser.switch_to.window(handle)
    # print(browser.current_window_handle)
    # handles = browser.window_handles
    # print(handles)
    doc = browser.page_source
    emails = re.findall('[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+ ', doc)
    # emails = re.findall(r'[\w]+@[\w\.-]+', doc)
    for index, email in enumerate(emails):
        # ws.write(index, 0, email)
        print(email)
    wb.save('百度联系邮箱.xls')
    print('提取完成')
finally:
    browser.quit()