from selenium.webdriver import Chrome,ActionChains

class test001:
    driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://www.naukri.com/')

    act = ActionChains(driver)
    element1 = driver.find_element_by_xpath("//div[contains(text(),'Recruiters')]")
    act.move_to_element(element1).perform()
    element2 = driver.find_element_by_xpath("// a[ @ title = 'Browse All Recruiters']")
    act.move_to_element(element2).click().perform()
