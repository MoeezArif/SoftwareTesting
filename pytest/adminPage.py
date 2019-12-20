
import unittest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import Select

class AdminPage():

    def __init__(self,driver):
        self.driver=driver

        self.type_approve_xpath='//*[@id="home-section"]/div/div/div/div/div/table/tbody/tr/td[13]/button'
        self.type_reject_xpath = '//*[@id="home-section"]/div/div/div/div/div/table/tbody/tr/td[14]/button'
        self.btn_logout_xpath='//*[@id="navbarCollapse"]/form/input'


    def selectApprove(self):
        self.driver.find_element_by_xpath(self.type_approve_xpath).click()

    def selectReject(self):
        self.driver.find_element_by_xpath(self.type_reject_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()