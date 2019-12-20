
import unittest
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import Select

class SignupPage():

    def __init__(self,driver):
        self.driver=driver

        self.type_fullname_id='fullname'
        self.email_textbox_id='email'
        self.textbox_password_id = 'password'
        self.textbox_confirmpassword_id = 'confirmpassword'
        self.btn_signUp_xpath='//*[@id="home-section"]/div/div/div/div/div/div/form/button'


    #def setUp(self):
        #self.driver = webdriver.Chrome('F:\dev\chromedriver.exe')

    def enterFullname(self,name):
        self.driver.find_element_by_id(self.type_fullname_id).clear()
        self.driver.find_element_by_id(self.type_fullname_id).send_keys(name)

    def enterEmail(self,mail):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(mail)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def enterConfirmPassword(self, cnfpassword):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(cnfpassword)

    def signUpClick(self):
        self.driver.find_element_by_xpath(self.btn_signUp_xpath).click()