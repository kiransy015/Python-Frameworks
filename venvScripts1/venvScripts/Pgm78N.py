from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()

typefield = driver.find_element_by_name('email').get_attribute('type')

if typefield=='password':
    print("Its password field")
else:
    print("Its not password field")
driver.close()
