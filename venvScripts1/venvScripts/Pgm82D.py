from selenium.webdriver import Chrome,ActionChains

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://www.google.co.in/')

    element = driver.find_element_by_xpath("//a[contains(text(),'Gmail')]")
    act = ActionChains(driver)
    act.click(element).perform()