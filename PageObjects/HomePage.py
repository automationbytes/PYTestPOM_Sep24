from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage():
    appLogo_webElement_xpath = "//div[text()='Swag Labs']"
    filter_select_xpath = "//select[@data-test='product-sort-container']"
    openMenu_webElement_css = '#react-burger-menu-btn'
    logOut_webLink_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver
        #self.driver = webdriver.Chrome()

    def verifyLogo(self):
        return self.driver.find_element(By.XPATH,self.appLogo_webElement_xpath).is_displayed()

    def selectFilterDropdown(self,value):
        dropdown = Select(self.driver.find_element(By.XPATH,self.filter_select_xpath))
        dropdown.select_by_visible_text(value)

    def clickLogout(self):
        self.driver.find_element(By.CSS_SELECTOR,self.openMenu_webElement_css).click()
        self.driver.find_element(By.XPATH,self.logOut_webLink_xpath).click()