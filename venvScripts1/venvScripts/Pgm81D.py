from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://www.facebook.com/')

    month_sel = Select(driver.find_element_by_id('month'))
    options = month_sel.options

    size = len(options)

    month_sel.select_by_index(size-1)
    driver.close()


