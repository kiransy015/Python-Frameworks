from Lib.ui.homepage import homepage
from Lib.util import Driverinstance
from Lib.util import TimeOutHandler
import unittest

class TestLogin:

    def setUp(self):
        self.driver = Driverinstance.getbrowserInstance()
        print("Driver :",self.driver)
        self.homepage = homepage(self.driver)

    def tearDown(self):
        self.driver.close


    def test_Searchtext(self):
        self.homepage.wait_for_PageLoad()
        self.homepage.get_Google_textbox().send_keys('selenium')
        self.homepage.get_Search_Btn().click()