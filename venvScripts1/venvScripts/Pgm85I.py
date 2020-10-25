import unittest
from selenium.webdriver import Chrome

from venvScripts.facebookLoginPage import facebookLoginPage


class test_facebookLogin_S135766(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.facebook.com/')
        self.login = facebookLoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_tc183265(self):
        self.login.get_username_textbox().send_keys('invalid')
        self.login.get_password_textbox().send_keys('invalid')
        self.login.get_login_button().click()
