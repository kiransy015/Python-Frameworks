from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def wait_for_elementToBeClickable(driver,element):
    wait = WebDriverWait(driver=driver,timeout=30)
    wait.until(expected_conditions.element_to_be_clickable(element))

def wait_for_elementToBeVisible(driver,element):
    wait = WebDriverWait(driver=driver,timeout=30)
    wait.until(expected_conditions.visibility_of(element))


