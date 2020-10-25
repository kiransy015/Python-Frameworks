import pytest
from _pytest.main import pytest_addoption

def pytest_addoption(parser):
    parser.addoption("--browser",default="firefox")
    parser.addoption("--env",default="test")
    parser.addoption("--system",default="windows")

