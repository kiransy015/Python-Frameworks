from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_name('q').send_keys('Java')
driver.find_element_by_name('q').send_keys(Keys.CONTROL,'a',Keys.DELETE)
driver.find_element_by_name('q').send_keys('Selenium')
driver.close()
