from selenium.webdriver.common.by import By
import unittest

class LoginPage(unittest.TestCase):
    LOGIN_USER = (By.ID, 'loginFrm_loginname')
    PASS_USER = (By.ID, 'loginFrm_password')
    BTN_LOGIN = (By.CSS_SELECTOR, 'button[title="Login"]')

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.LOGIN_USER).send_keys(username)
        self.driver.find_element(*self.PASS_USER).send_keys(password)
        self.driver.find_element(*self.BTN_LOGIN).click()
