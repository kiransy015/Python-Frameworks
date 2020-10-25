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

    print(type(options))
    print(options)

    for i in range(0,size):
        print(options[i].text)

    driver.close()