import unittest
import time

from selenium.webdriver import Chrome

from venvScripts.loginPage import LoginPage


class test_login_S135766(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://demo.actitime.com/login.do")
        self.login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_invalid_tc183265(self):
        self.login.wait_for_login_page_to_load()
        self.login.get_username_textbox().send_keys('Invalid')
        self.login.get_password_textbox().send_keys('Invalid')
        self.login.get_login_button().click();
        expected_err_msg = 'Username or Password is invalid. Please try again.'
        actual_err_msg = self.login.get_login_error_msg().text
        assert expected_err_msg==actual_err_msg


