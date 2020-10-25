import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://www.facebook.com/')

    day_sel = Select(driver.find_element_by_id('day'))
    day_sel.select_by_value('20')

    month_sel = Select(driver.find_element_by_id('month'))
    month_sel.select_by_index('5')

    year_sel = Select(driver.find_element_by_id('year'))
    year_sel.select_by_visible_text('2017')
    driver.close()