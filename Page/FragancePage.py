import unittest
from selenium.webdriver.common.by import By

class FragancePage(unittest.TestCase):
    SELECTOR = (By.ID, 'sort')
    ORDEN = (By.CSS_SELECTOR,'option[value="p.price-DESC"]')
    NAME = (By.LINK_TEXT, 'link-text')

    def __init__(self, driver):
        self.driver = driver

    def get_selector_option(self):
        return self.driver.find_element(*FragancePage.SELECTOR)

    def get_option(self):
        return self.driver.find_element(*FragancePage.ORDEN)

    def fraganceName(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, 'div.grid>div:nth-child('+num+') a.prdocutname')
