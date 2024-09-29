import pytest
from selenium import webdriver

from Util.generateLogs import LogGenerator
from Util.readConfig import readConfig

logger = LogGenerator.loggen()


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.firefox

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser",help= "Choose the browser: chrome, edge or firefox")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")