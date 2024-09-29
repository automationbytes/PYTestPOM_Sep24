import pytest
from selenium import webdriver

from Util.readConfig import readConfig


class TestDemo:


   # @pytest.fixture()
    def test_prestep(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(int(readConfig.getConfig("commoninfo","timeout")))
        self.driver.get(readConfig.getConfig("commoninfo","baseURL"))


