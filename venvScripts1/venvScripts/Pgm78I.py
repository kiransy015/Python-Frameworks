from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
element = driver.find_element_by_name('email')
position = element.location
print(position)
print('X :',position['x'])
print('Y :',position['y'])
driver.close()
