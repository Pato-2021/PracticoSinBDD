import unittest
from selenium.webdriver.common.by import By

class MyAccountPage(unittest.TestCase):
    TITLE = (By.CSS_SELECTOR, 'h1 span.maintext')
    FRAGANCE = (By.CSS_SELECTOR, 'ul.categorymenu>li:nth-of-type(5)')
    WOMEN = (By.LINK_TEXT, 'Women')

    def __init__(self, driver):
        self.driver = driver

    def checkTitle(self):
        return self.driver.find_element(*self.TITLE).text

    def getFraganceBtn(self):
        return self.driver.find_element(*MyAccountPage.FRAGANCE)

    def getFragance(self):
        return self.driver.find_element(*MyAccountPage.WOMEN)
