from selenium.webdriver import Chrome
import time
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
print(driver.find_element_by_xpath("(//a[@href='https://mail.google.com/mail/?tab=rm'])[1]").text)

