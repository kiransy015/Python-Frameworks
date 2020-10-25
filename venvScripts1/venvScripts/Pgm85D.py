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

    def test_gmail_link_of_google(self):
        driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com")
        assert driver.find_element_by_link_text('Gmail').is_enabled()
        driver.close()

    def test_search_textbox_of_google(self):
        driver = Chrome("C:\\Kiran Kumar SY\\Python\\Softwares\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com")
        textbox = driver.find_element_by_name('q')
        assert textbox.get_attribute('maxlength')=='2048'
        textbox.send_keys('Java')
        assert textbox.get_attribute('value')=='Java'
        driver.close()

