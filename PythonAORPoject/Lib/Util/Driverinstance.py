import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Ie
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def getDriverInstance():
    testbrowser = pytest.config.option.browser
    testenv = pytest.config.option.env

    if(testbrowser.lower()=="chrome"):
        driver = Chrome("C:/Kiran Kumar SY/Python/PythonAORPoject/BrowserServers/chromedriver.exe")
    elif(testbrowser.lower()=="firefox"):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        driver = webdriver.Firefox(capabilities=cap, executable_path="C:/Kiran Kumar SY/Python/PythonAORPoject/BrowserServers/geckodriver.exe")
    else:
        return None

    driver.maximize_window()
    driver.implicitly_wait(30)
    if(testenv.lower()=='test'):
        driver.get("https://135.250.138.235:9443/aor-portal/#/")
    elif(testenv.lower()=='prod'):
        driver.get("https://135.250.138.235:9443/aor-portal/#/")



    return driver

