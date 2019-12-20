
import unittest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import Select

class DeleteFlightPage():

    def __init__(self,driver):
        self.driver=driver

        self.type_flightno_name='flightno'
        self.type_date_name = 'dates'
        self.btn_deleteflight_xpath='//*[@id="home-section"]/div/div/div/div/div[2]/div/div/form/input'
        self.btn_logout_xpath='//*[@id="navbarCollapse"]/form/input'


    def selectFlightNo(self,number):
        dd = self.driver.find_element_by_name(self.type_flightno_name)
        d = Select(dd)
        d.select_by_visible_text(number)

    def enterDate(self,date):
        self.driver.find_element_by_name(self.type_date_name).send_keys(date)


    def deleteFlight(self):
        self.driver.find_element_by_xpath(self.btn_deleteflight_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()