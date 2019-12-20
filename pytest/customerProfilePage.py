
import unittest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import Select

class CustomerProfilePage():

    def __init__(self,driver):
        self.driver=driver

        self.type_departure_id='departure'
        self.type_arrival_id='arrival'
        self.type_date_id = 'dates'
        self.type_selectclass_id = 'selectclass'
        self.type_adult_id = 'adults'
        self.type_children_id = 'children'
        self.btn_availability_xpath='//*[@id="home-section"]/div/div/div/div/div[2]/div/div/form/input'
        self.btn_logout_xpath='//*[@id="navbarCollapse"]/form/input'



    def enterDeparture(self,departure):
        self.driver.find_element_by_name(self.type_departure_id).clear()
        self.driver.find_element_by_name(self.type_departure_id).send_keys(departure)

    def enterArrival(self,arrival):
        self.driver.find_element_by_name(self.type_arrival_id).clear()
        self.driver.find_element_by_name(self.type_arrival_id).send_keys(arrival)

    def enterDate(self,date):
        self.driver.find_element_by_name(self.type_date_id).send_keys(date)

    def enterClass(self,classType):
        dd = self.driver.find_element_by_name(self.type_selectclass_id)
        d = Select(dd)
        d.select_by_visible_text(classType)

    def enterAdultSeats(self, adult):
        self.driver.find_element_by_name(self.type_adult_id).clear()
        self.driver.find_element_by_name(self.type_adult_id).send_keys(adult)

    def enterChildrenSeats(self, children):
        self.driver.find_element_by_name(self.type_children_id).clear()
        self.driver.find_element_by_name(self.type_children_id).send_keys(children)


    def checkAvailabilty(self):
        self.driver.find_element_by_xpath(self.btn_availability_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()