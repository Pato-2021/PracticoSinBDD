from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import unittest
from Page.MyAccountPage import *
from Page.FragancePage import *
import pytest
import time
import json

class FraganceTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("../Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://automationteststore.com/")
        cls.driver.maximize_window()

    @classmethod
    def test_selector_fragance(self):
        driver = self.driver
        ## Selecciono women desde fragrance
        myAccountPage = MyAccountPage(driver)
        hover = ActionChains(driver).move_to_element(myAccountPage.getFraganceBtn())
        hover.perform()
        myAccountPage.getFragance().click()
        ## Selecciono por orden
        fragancePage = FragancePage(driver)
        fragancePage.get_selector_option().click()
        fragancePage.get_option().click()
        print('TEST: Paso la seleccion por orden')
        ## leer json
        file = open('../Data/fragance_data.json', 'r')
        data = file.read()
        obj = json.loads(data)
        list = obj['fragances']

        for i in range(len(list)):
            assert fragancePage.fraganceName(str(i+1)).text == list[i].get('name').upper()
            print('Name: '+str(i+1)+';  '+ list[i].get('name'))
        print('Todos los nombres estan checheados')


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")