import unittest
from selenium.webdriver import Chrome

class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")


    def tearDown(self):
        self.driver.close()


    def test_title_of_google(self):
        actual_title = self.driver.title
        expected_title = 'Google'
        assert actual_title==expected_title

    def test_gmail_link_of_google(self):
        assert self.driver.find_element_by_link_text('Gmail').is_enabled()

    def test_search_textbox_of_google(self):
        textbox = self.driver.find_element_by_name('q')
        assert textbox.get_attribute('maxlength')=='2048'
        textbox.send_keys('Java')
        assert textbox.get_attribute('value')=='Java'



