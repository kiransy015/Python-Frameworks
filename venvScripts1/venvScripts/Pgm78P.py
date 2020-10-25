from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.facebook.com/")
print(driver.find_element_by_xpath("//span[text()='Create an account']").value_of_css_property('font-size'))
print(driver.find_element_by_xpath("//span[text()='Create an account']").value_of_css_property('color'))
driver.close()
