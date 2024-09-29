import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Util.generateLogs import LogGenerator
from Util.readConfig import readConfig



class TestDemo:
    logger = LogGenerator.loggen()

    @pytest.fixture()
    def login(self,setup):
        self.logger.info("------------Pre Step-----------------")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(int(readConfig.getConfig("commoninfo","timeout")))
        self.logger.info("------------URL Launch-----------------")
        self.driver.get(readConfig.getConfig("commoninfo","baseURL"))
        lp = LoginPage(self.driver)
        lp.enterUsername(readConfig.getConfig("commoninfo","username"))
        lp.enterPassword(readConfig.getConfig("commoninfo","password"))
        lp.clickLogin()


    def test_dropdown_high2low(self,login):
        self.logger.info("------------Home Launch-----------------")
        hp = HomePage(self.driver)
        if hp.verifyLogo():
            assert True
        else:
            self.driver.save_screenshot("logo.png")
        self.logger.info("------------Filter dropdown-----------------")
        hp.selectFilterDropdown("Price (high to low)")


