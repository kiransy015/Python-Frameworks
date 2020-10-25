from selenium.webdriver import Chrome
driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_link_text('Gmail').click()
driver.close()
