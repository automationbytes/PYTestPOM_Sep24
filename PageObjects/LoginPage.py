from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    username_editbox_id = 'user-name'
    password_editbox_name = 'password'
    login_button_name = 'login-button'


    def __init__(self,driver):
        self.driver = driver


    def enterUsername(self,user):
        self.driver.find_element(By.ID,self.username_editbox_id).send_keys(user)

    def enterPassword(self,password):
        self.driver.find_element(By.NAME,self.password_editbox_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.NAME,self.login_button_name).click()