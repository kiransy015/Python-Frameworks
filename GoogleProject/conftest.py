import pytest
from _pytest.main import pytest_addoption

def pytest_addoption(parser):
    parser.addoption('--browser',default="chrome")
    parser.addoption('--url',default="test")