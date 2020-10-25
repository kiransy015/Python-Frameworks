from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
maxlen = driver.find_element_by_name('q').get_attribute('maxlength')

if maxlen=='2048':
    print("PASSED")
else:
    print("FAILED")
driver.close()