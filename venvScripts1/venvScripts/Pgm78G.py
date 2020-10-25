from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_name('email').send_keys('kiran015')
driver.find_element_by_name('email').send_keys(Keys.CONTROL,'a')
driver.find_element_by_name('email').send_keys(Keys.CONTROL,'c')
driver.find_element_by_name('email').send_keys(Keys.TAB,Keys.CONTROL,'v')
driver.close()
