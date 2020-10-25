from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Ie
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


def getbrowserInstance(self):
    testbrowser = pytest.config.option.browser;
    testenv = pytest.config.option.url;

    if testbrowser.lower()=="chrome":
        driver = Chrome("C:/Kiran Kumar SY/Python/GoogleProject/BrowserServers/chromedriver.exe")
    elif testbrowser.lower()=="firefox":
        driver = Firefox("C:/Kiran Kumar SY/Python/GoogleProject/BrowserServers/geckodriver.exe")
    else:
        print("Invalid browser option")
        return None

    driver.maximize_window()
    driver.implicit_wait(30)

    if testbrowser.lower()=='test':
        driver.get("https://www.google.com/")
    elif testbrowser.lower()=='prod':
        driver.get("https://www.google.com/")
    else:
        print("Invalid env option")
        return None



    return driver



