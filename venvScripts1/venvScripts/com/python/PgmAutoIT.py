import unittest
from selenium.webdriver import Chrome
import subprocess
import time

class TestLoginU15678(unittest.TestCase):
    def test_valid_login(self):
        subprocess.Popen('C:/Kiran Kumar SY/Python/UploadFile.exe')
        driver = Chrome('C:\Kiran Kumar SY\Python\Softwares\chromedriver.exe')
        driver.maximize_window()
        driver.get('file:///C:/Kiran%20Kumar%20SY/Python/Sample.html')
        driver.find_element_by_xpath("//input[@type='file']").click()