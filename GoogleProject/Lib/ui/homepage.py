from Lib.util import TimeOutHandler


class homepage:

    def __init__(self,driver):
        self.driver = driver

    def wait_for_PageLoad(self):
        element = self.driver.find_element_by_name("q")
        TimeOutHandler.wait_for_elementToBeClickable(self.driver,element)

    def get_Google_textbox(self):
        try:
            return self.driver.find_element_by_name("q")
        except:
            return None

    def get_Search_Btn(self):
        try:
            return self.driver.find_element_by_xpath("(//input[@value='Google Search'])[2]")
        except:
            return None