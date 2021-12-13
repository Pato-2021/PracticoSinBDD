from selenium import webdriver
import time
from Page.LoginPage import *
from Page.PrincipalPage import *
from Page.MyAccountPage import *
import unittest

class LoginTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://automationteststore.com/")
        cls.driver.maximize_window()

    def test_login(self):
        principalPage = PrincipalPage(self.driver)
        loginPage = LoginPage(self.driver)
        myAccountPage = MyAccountPage(self.driver)

        ## Step 1: Hacemos click en el boton Login or Register
        principalPage.iraLoginPage()
        time.sleep(2)

        ## Step 2: Completamos con usuario y pasword
        loginPage.login('PatoM', 'Automatizacion')

        ## Step 3: Chequeamos la cuenta
        assert myAccountPage.checkTitle() == 'MY ACCOUNT'
        print('TEST: Valid Login - Check My Account title')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')