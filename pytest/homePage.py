import unittest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import Select


class HomePage():

    def __init__(self,driver):
        self.driver=driver

        self.btn_signUp_xpath='//*[@id="navbarCollapse"]/a[1]'
        self.btn_signIn_xpath='//*[@id="navbarCollapse"]/a[2]'


    def clickSignIn(self):
        self.driver.find_element_by_xpath(self.btn_signIn_xpath).click()

    def clickSignUp(self):
        self.driver.find_element_by_xpath(self.btn_signUp_xpath).click()

