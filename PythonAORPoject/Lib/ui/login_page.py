from Lib.Util import TimeOutHandler

class loginpage():

    def __init__(self,driver):
        self.driver = driver

    def waitforpagetoload(self):
        TimeOutHandler.waitforVisibilityOfElement(self.driver,self.driver.find_element_by_id('target2'))

    def getusernametextfield(self):
        try:
            return self.driver.find_element_by_id('target2')
        except:
            return None

    def getpasswordtextfield(self):
        try:
            return self.driver.find_element_by_id('login-password')
        except:
            return None

    def getloginBtn(self):
        try:
            return self.driver.find_element_by_id('sbtbtn')
        except:
            return None

