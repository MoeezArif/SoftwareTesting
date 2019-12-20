
import unittest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import Select

class AddFlightPage():

    def __init__(self,driver):
        self.driver=driver

        self.type_flightno_name='flightno'
        self.type_arrival_name='arrival'
        self.type_departure_name = 'departure'
        self.type_date_name = 'dates'
        self.type_time_name = 'time'
        self.type_economyseat_name = 'economyseat'
        self.type_economyprice_name='economyprice'
        self.type_businessseat_name = 'businessseat'
        self.type_businessprice_name = 'businessprice'
        self.type_firstseat_name = 'firstseat'
        self.type_firstprice_name = 'firstprice'
        self.btn_addflight_xpath='//*[@id="home-section"]/div/div/div/div/div[2]/div/div/form/input'
        self.btn_logout_xpath='//*[@id="navbarCollapse"]/form/input'


    def enterFlightNo(self,number):
        self.driver.find_element_by_name(self.type_flightno_name).clear()
        self.driver.find_element_by_name(self.type_flightno_name).send_keys(number)

    def enterDeparture(self,departure):
        self.driver.find_element_by_name(self.type_departure_name).clear()
        self.driver.find_element_by_name(self.type_departure_name).send_keys(departure)

    def enterArrival(self,arrival):
        self.driver.find_element_by_name(self.type_arrival_name).clear()
        self.driver.find_element_by_name(self.type_arrival_name).send_keys(arrival)

    def enterDate(self,date):
        self.driver.find_element_by_name(self.type_date_name).send_keys(date)

    def enterTime(self,time):
        self.driver.find_element_by_name(self.type_time_name).send_keys(time)

    def enterEconomySeat(self,seat):
        self.driver.find_element_by_name(self.type_economyseat_name).clear()
        self.driver.find_element_by_name(self.type_economyseat_name).send_keys(seat)

    def enterEconomyPrice(self,price):
        self.driver.find_element_by_name(self.type_economyprice_name).clear()
        self.driver.find_element_by_name(self.type_economyprice_name).send_keys(price)

    def enterBusinessSeat(self, seat):
        self.driver.find_element_by_name(self.type_businessseat_name).clear()
        self.driver.find_element_by_name(self.type_businessseat_name).send_keys(seat)

    def enterBusinessPrice(self, price):
        self.driver.find_element_by_name(self.type_businessprice_name).clear()
        self.driver.find_element_by_name(self.type_businessprice_name).send_keys(price)

    def enterFirstSeat(self, seat):
        self.driver.find_element_by_name(self.type_firstseat_name).clear()
        self.driver.find_element_by_name(self.type_firstseat_name).send_keys(seat)

    def enterFirstPrice(self, price):
        self.driver.find_element_by_name(self.type_firstprice_name).clear()
        self.driver.find_element_by_name(self.type_firstprice_name).send_keys(price)


    def addFlight(self):
        self.driver.find_element_by_xpath(self.btn_addflight_xpath).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()