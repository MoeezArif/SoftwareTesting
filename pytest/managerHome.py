import unittest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import Select


class ManagerHomePage():

    def __init__(self,driver):
        self.driver=driver

        self.btn_addflight_xpath='//*[@id="navbarCollapse"]/ul/li[2]/a'
        self.btn_updateflight_xpath='//*[@id="navbarCollapse"]/ul/li[3]/a'
        self.btn_deleteflight_xpath = '//*[@id="navbarCollapse"]/ul/li[4]/a'
        self.btn_logout_xpath='//*[@id="navbarCollapse"]/form/input'


    def addFlight(self):
        self.driver.find_element_by_xpath(self.btn_addflight_xpath).click()

    def updateFlight(self):
        self.driver.find_element_by_xpath(self.btn_updateflight_xpath).click()

    def deleteFlight(self):
        self.driver.find_element_by_xpath(self.btn_deleteflight_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()
