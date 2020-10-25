from Lib.Util import TimeOutHandler


class homepage:

    def __init__(self,driver):
        self.driver = driver

    def waitforpageToLoad(self):
        TimeOutHandler.waitforVisibilityOfElement(self.driver,self.driver.find_element_by_xpath("// button[div[span[text() = 'ACCEPT']]]"))

    def getAccrptBtn(self):
        try:
            return self.driver.find_element_by_xpath("// button[div[span[text() = 'ACCEPT']]]")
        except:
            return None

    def getaorlogoutBtn(self):
        try:
            return self.driver.find_element_by_xpath("//button[contains(@id,'logout-button')]")
        except:
            return None

    def getPanelDropdown(self):
        try:
            return self.driver.find_element_by_xpath(".//*[contains(@id,'userAccount-button')]")
        except:
            return None

    def getFlyoutMenu(self):
        try:
            return self.driver.find_element_by_xpath("//button[contains(@id,'sideDrawerButton-button')]")
        except:
            return None

    def getEventsLink(self):
        try:
            return self.driver.find_element_by_xpath("//li/div/div[text()='Events']")
        except:
            return None


