from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.facebook.com/")
element = driver.find_element_by_name('email')
size = element.size
print(size)
print('Height =',size['height'])
print('Width =',size['width'])
driver.close()
