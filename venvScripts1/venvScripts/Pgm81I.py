from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://www.facebook.com/')

    mon_sel = Select(driver.find_element_by_id('month'))
    val = mon_sel.is_multiple

    if val:
        print("Dropdown is a multi select")
    else:
        print("Dropdown is not multi select")

    driver.close()