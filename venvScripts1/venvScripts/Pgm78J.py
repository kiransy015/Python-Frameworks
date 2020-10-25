from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
email_textbox = driver.find_element_by_name('email')
password_textbox = driver.find_element_by_name('pass')
# email_textboxsize = email_textbox.size
print(email_textbox.size['height'])
if email_textbox.size['height']==password_textbox.size['height'] and email_textbox.size['width']==password_textbox.size['width']:
    print('Email and Password textbox size are matching')
else:
    print('Email and Password textbox size are not matching')
driver.close()