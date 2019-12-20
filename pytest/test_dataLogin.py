import pytest
import time
import selenium.webdriver as webdriver
from homePage import HomePage
from loginPage import LoginPage
from customerProfilePage import CustomerProfilePage

@pytest.mark.parametrize('value_A,value_B', [
    # each element of this list will provide values for the
    # topics "value_A" and "value_B" of the test and will
    # generate a stand-alone test case.
    ('mo@gmail.com', 12345),
    ('mo@gmail.com', 2),
    ('tahir@gmail.com', 1234),
    ('tom6@gmail.com', 1234),
    ('raja@gmail.com', 2),
    ('moeez@@gmail.com', 2),
    ('nawaz@gmail.com', 2),
    ('nawaz@gmail.com', 2)
])
def test_func(value_A, value_B):
    global driver
    driver = webdriver.Chrome('F:\dev\chromedriver.exe')
    driver.get('http://localhost:9090/WebSE/')

    home = HomePage(driver)
    home.clickSignIn()
    page1=driver.current_url
    login = LoginPage(driver)
    time.sleep(1)
    login.selectUserType('Customer')
    time.sleep(1)
    login.enterEmail(value_A)
    time.sleep(1)
    login.enterPassword(value_B)
    time.sleep(1)
    login.signInClick()
    time.sleep(1)
    customer=CustomerProfilePage(driver)
    customer.logout()
