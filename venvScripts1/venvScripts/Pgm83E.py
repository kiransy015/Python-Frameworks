import time
from selenium.webdriver import Chrome

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://www.yatra.com/')

    time.sleep(10)
    driver.find_element_by_id('BE_flight_origin_date').click()
    driver.find_element_by_id('20/04/2019').click()