from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
status = driver.find_element_by_name('reg_email_confirmation__').is_displayed()

if status==True:
    print('Element is visible')
else:
    print('Element is not visible')
driver.close()