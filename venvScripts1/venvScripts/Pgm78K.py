from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
email_textbox_pos = driver.find_element_by_name('email').location
pass_textbox_pos = driver.find_element_by_name('email').location


if email_textbox_pos['y']==pass_textbox_pos['y']:
    print('Textboxes are arranged horizontally')
else:
    print('Textboxes are not arranged horizontally')
driver.close()