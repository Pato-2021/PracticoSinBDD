import unittest
from selenium.webdriver.common.by import By

class PrincipalPage(unittest.TestCase):
    BTN_REGISTER = (By.LINK_TEXT, 'Login or register')

    def __init__(self, driver):
        self.driver = driver

    def iraLoginPage(self):
        self.driver.find_element(*self.BTN_REGISTER).click()
