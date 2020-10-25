from selenium.webdriver import Chrome

driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)

driver.get('https://www.javascriptkit.com/javatutors/alert2.shtml')

driver.switch_to_frame('aswift_0')
driver.switch_to_frame('google_ads_frame1')
driver.find_element_by_id('cbb').click()
driver.switch_to_default_content()