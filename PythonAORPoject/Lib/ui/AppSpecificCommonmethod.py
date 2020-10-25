from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Lib.Util import TimeOutHandler


def aorLogin(login,username,password):
    login.getusernametextfield().send_keys(username)
    login.getpasswordtextfield().send_keys(password)
    login.getloginBtn().click()


def aorLoginThroughSendKeys(driver,login,username,password):
    actions = ActionChains(driver)
    actions.move_to_element(login.getusernametextfield()).click().send_keys(username).perform()
    actions.move_to_element(login.getpasswordtextfield()).click().perform()
    actions.send_keys(password,Keys.ENTER).perform()


def navigateToAPage(driver,home):
    TimeOutHandler.waitforVisibilityOfElement(driver, home.getFlyoutMenu())
    home.getFlyoutMenu().click()
    TimeOutHandler.waitforVisibilityOfElement(driver,home.getEventsLink())
    home.getEventsLink().click()






