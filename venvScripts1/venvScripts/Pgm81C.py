from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://www.facebook.com/')

    exp_month = 'Nov'
    month_sel = Select(driver.find_element_by_id('month'))
    options = month_sel.options
    size = len(options)

    for i in range(0,size):
        if options[i].text==exp_month:
            month_sel.select_by_visible_text(options[i].text)
            break

    driver.close()