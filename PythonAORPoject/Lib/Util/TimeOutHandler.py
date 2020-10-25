from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def waitforVisibilityOfElement(driver,webelement):
    wait = WebDriverWait(timeout=30,driver=driver)
    wait.until(expected_conditions.visibility_of(webelement))

def waitforElementToBeClickable(driver,element):
    wait = WebDriverWait(timeout=30,driver=driver)
    wait.until(expected_conditions.element_to_be_clickable(element))
