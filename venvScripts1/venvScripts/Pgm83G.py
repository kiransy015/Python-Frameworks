import time
from selenium.webdriver import Chrome

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://demo.actitime.com/login.do')

    time.sleep(10)
    print("Title of main window :",driver.title)
    driver.find_element_by_link_text('actiTIME Inc.').click()

    windows = driver.window_handles
    driver.switch_to_window(windows[1])
    print("Title of child window :", driver.title)
    driver.find_element_by_xpath("//a[text()='Try Free']").click()
    print("Title of next window :", driver.title)
    driver.close()
    driver.switch_to_window(windows[0])
    print("Title of main window :", driver.title)
    driver.close()