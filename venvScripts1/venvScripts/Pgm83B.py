import time
from selenium.webdriver import Chrome

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('http://www.javascriptkit.com/javatutors/alert2.shtml')

    time.sleep(10)
    driver.find_element_by_name('B3').click()

    alt = driver.switch_to_alert()
    msg = alt.text
    print(msg)
    alt.dismiss()
    driver.close()