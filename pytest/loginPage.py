
import unittest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import Select

class LoginPage():

    def __init__(self,driver):
        self.driver=driver

        self.type_dropdown_id='usertype'
        self.email_textbox_id='email'
        self.email_textbox_password = 'password'
        self.btn_signIn_xpath='//*[@id="home-section"]/div/div/div/div/div/div/form/button'


    #def setUp(self):
        #self.driver = webdriver.Chrome('F:\dev\chromedriver.exe')

    def selectUserType(self,user):
        dd = self.driver.find_element_by_name(self.type_dropdown_id)
        d = Select(dd)
        d.select_by_visible_text(user)

    def enterEmail(self,mail):
        self.driver.find_element_by_name(self.email_textbox_id).clear()
        self.driver.find_element_by_name(self.email_textbox_id).send_keys(mail)

    def enterPassword(self, password):
        self.driver.find_element_by_name(self.email_textbox_password).clear()
        self.driver.find_element_by_name(self.email_textbox_password).send_keys(password)


    def signInClick(self):
        self.driver.find_element_by_xpath(self.btn_signIn_xpath).click()