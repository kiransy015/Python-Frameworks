from selenium.webdriver import Chrome

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://www.flipkart.com/')

    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
    driver.execute_script("window.scroll(0,10000)")