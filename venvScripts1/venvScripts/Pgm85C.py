import unittest
from selenium.webdriver import Chrome

class TestGoogle(unittest.TestCase):
    def test_title_of_google(self):
        driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com")
        actual_title = driver.title
        expected_title = 'Google'
        assert actual_title==expected_title
        driver.close()