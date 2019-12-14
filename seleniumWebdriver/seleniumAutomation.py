import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

user="mo@gmail.com"
id="12345"
browser=webdriver.Chrome('F:\dev\chromedriver.exe')
browser.get('http://localhost:9090/WebSE/')
time.sleep(2)

def signUp():
    #signUp customer
    #login button
    page1=browser.current_url
    select1='//*[@id="navbarCollapse"]/a[1]'
    browser.find_element_by_xpath(select1).click()
    time.sleep(1)
    #send full name
    browser.find_element_by_id('fullname').send_keys('tom2')
    time.sleep(1)
    browser.find_element_by_id('email').send_keys('tom2@gmail')
    time.sleep(1)
    browser.find_element_by_name('password').click()
    # Click on the "Alert" button to generate the Simple Alert


    # Switch the control to the Alert window
    obj = browser.switch_to.alert


    time.sleep(2)

    # use the accept() method to accept the alert
    obj.accept()
    time.sleep(1)
    browser.find_element_by_name('password').send_keys(id)
    time.sleep(1)
    browser.find_element_by_name('confirmpassword').send_keys(id)
    time.sleep(1)
    #click signUP
    browser.find_element_by_xpath('//*[@id="home-section"]/div/div/div/div/div/div/form/button').click()
    time.sleep(1)
    if page1==browser.current_url:
        print('Wrong Credentials')
        print('SignUp Test Failed')
    else:
        print('SignUp Test Successfull')
    time.sleep(20)

def login():
    #login customer
    browser.implicitly_wait(2)
    #login button
    select1='//*[@id="navbarCollapse"]/a[2]'
    browser.find_element_by_xpath(select1).click()
    time.sleep(1)
    #select user drop down
    select1='//*[@id="home-section"]/div/div/div/div/div/div/form/select'
    dd=browser.find_element_by_xpath(select1)
    d=Select(dd)
    d.select_by_visible_text('Customer')
    time.sleep(2)
    #send email
    browser.find_element_by_xpath('//*[@id="home-section"]/div/div/div/div/div/div/form/input[1]').send_keys('mo@gmail.com')
    time.sleep(1)
    #send password
    browser.find_element_by_xpath('//*[@id="home-section"]/div/div/div/div/div/div/form/input[2]').send_keys(id)
    time.sleep(1)
    #click aign in button
    browser.find_element_by_xpath('//*[@id="home-section"]/div/div/div/div/div/div/form/button').click()
    time.sleep(2)

def bookFlight():
    #login customer
    time.sleep(2)
    #login button
    select1='departure'
    browser.find_element_by_name(select1).send_keys('Lahore')
    time.sleep(1)
    #select user drop down
    select1='arrival'
    dd=browser.find_element_by_name(select1).send_keys('Karachi')
    time.sleep(1)
    #send email
    select1 = 'dates'
    browser.find_element_by_name(select1).send_keys('12192019')
    time.sleep(1)

    select1 = 'selectclass'
    dd = browser.find_element_by_name(select1)
    d = Select(dd)
    d.select_by_visible_text('Business')
    time.sleep(2)

    select1 = 'adults'
    browser.find_element_by_name(select1).send_keys(1)
    time.sleep(1)

    select1 = 'children'
    browser.find_element_by_name(select1).send_keys(0)
    time.sleep(1)


    browser.find_element_by_xpath('//*[@id="home-section"]/div/div/div/div/div[2]/div/div/form/input').click()
    time.sleep(100)

def redundant():
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="mdc-text-field__UID__26"]').send_keys(id)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/main/div/form/div[1]/button/span').click()
    time.sleep(20)

    #Select more
    select1='//*[@id="home-section"]/div/div/div/div/div/div/form/select'
    browser.find_element_by_xpath(select1).click()
    time.sleep(3)

    #premium fund screen
    select2='#tabpanel12 > li:nth-child(2) > a:nth-child(1)'
    browser.find_element_by_css_selector(select2).click()

    #click open my screen
    time.sleep(10)
    browser.switch_to_frame(browser.find_element_by_xpath('/html/body/div[3]/main/div/div/section[2]/div[1]/div/section[2]/iframe'))
    select3='/html/body/table/tbody/tr/td/form/a/table[3]/tbody/tr[2]/td[6]/a[1]'
    browser.find_element_by_xpath(select3).click()
    #switching between screens
    parent=browser.current_window_handle
    time.sleep(2)
    handles=browser.window_handles
    for handle in handles:
        browser.switch_to.window(handle)
        print(browser.title)
        if browser.title == 'Open My Screen':
            # open us growth
            select4 = 'select.PulldownTextC > option:nth-child(1)'
            time.sleep(3)
            browser.find_element_by_css_selector(select4).click()
            # click open
            time.sleep(5)
            select5 = '/html/body/form/table/tbody/tr[13]/td[2]/a[1]/img'
            browser.find_element_by_xpath(select5).click()

    time.sleep(5)
    browser.switch_to_window(parent)
    print(browser.title)
    #table page

    #browser.switch_to_frame(browser.find_element_by_xpath('/html/body/div[3]/main/div/div/section[2]/div[1]/div/section[2]/iframe'))
    #select view from drop down
    #select6='/html/body/table/tbody/tr/td/form/a/table[2]/tbody/tr[3]/td[3]/select'
    #time.sleep(5)
    #browser.find_element_by_xpath(select6).click()

    #select view
    time.sleep(15)
    browser.switch_to_frame(browser.find_element_by_xpath('/html/body/div[3]/main/div/div/section[2]/div[1]/div/section[2]/iframe'))
    dropd=browser.find_element_by_name('SelectView')

    drop_dd=Select(dropd)
    drop_dd.select_by_visible_text('View')

    #logic to compare the 2 columns
    time.sleep(10)
    nextCount=0
    while nextCount !=-1:
        columns = len(browser.find_elements_by_xpath('/html/body/table/tbody/tr/td/form/a/table[5]/tbody/tr/td[3]/a'))
        check11 = browser.find_element_by_xpath('/html/body/table/tbody/tr/td/form/a/table[5]/tbody/tr[4]/td[17]').text
        check12 = browser.find_element_by_xpath('/html/body/table/tbody/tr/td/form/a/table[5]/tbody/tr[4]/td[19]').text
        counter = 0
        for i in range(4,columns+1):
            check21 = browser.find_element_by_xpath('/html/body/table/tbody/tr/td/form/a/table[5]/tbody/tr['+str(i)+']/td[17]').text
            check22 = browser.find_element_by_xpath('/html/body/table/tbody/tr/td/form/a/table[5]/tbody/tr['+str(i)+']/td[19]').text
            if check11!=check21 or check12 != check22 :
                counter=0
                check11=check21
                check12=check22
            if check11 == check21 and check12 == check22 and counter ==0 :
                print(browser.find_element_by_xpath('/html/body/table/tbody/tr/td/form/a/table[5]/tbody/tr['+str(i)+']/td[17]').text)
                print(browser.find_element_by_xpath('/html/body/table/tbody/tr/td/form/a/table[5]/tbody/tr['+str(i)+']/td[19]').text)
                counter = counter + 1
                # select on base of turnover and %
                time.sleep(5)
                select6 = '/html/body/table/tbody/tr/td/form/a/table[5]/tbody/tr['+str(i)+']/td[3]/a'
                time.sleep(5)
                main_window = browser.current_window_handle
                link=browser.find_element_by_xpath(select6)
                # Open the link in a new tab by sending key strokes on the element
                # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
                link.send_keys(Keys.CONTROL + Keys.RETURN)
                time.sleep(10)
                # open my screen
                time.sleep(3)
                handles = browser.window_handles
                for handle in handles:
                    browser.switch_to.window(handle)
                    print(browser.title)
                    if browser.title != 'Morningstar: Premium Fund Screener':
                        sp = browser.title.split(' ')
                        time.sleep(10)
                        browser.get('https://portfolios.morningstar.com/fund/holdings?t=' + sp[0] + '&region=usa&culture=en-US')
                        time.sleep(15)
                        time.sleep(5)
                        select7 = '/html/body/div[1]/div[3]/div[2]/div[4]/a/span/span[1]'
                        browser.find_element_by_xpath(select7).click()
                        time.sleep(15)
                        select8 = '//*[@id="pager_top"]/div[3]/a/span'
                        browser.find_element_by_xpath(select8).click()

                        time.sleep(15)
                        # Close current tab
                        #browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                        # Put focus on current window which will be the window opener
                        browser.close()

                browser.switch_to_window(main_window)
                browser.switch_to_frame(browser.find_element_by_xpath('/html/body/div[3]/main/div/div/section[2]/div[1]/div/section[2]/iframe'))
                time.sleep(15)
        button=browser.find_element_by_xpath('/html/body/table/tbody/tr/td/form/a/table[4]/tbody/tr[2]/td[8]/div/a[11]')
        href_data = button.get_attribute('href')
        if href_data=='javascript:void(0)':
             nextCount=-1
        else:
            browser.find_element_by_xpath('/html/body/table/tbody/tr/td/form/a/table[4]/tbody/tr[2]/td[8]/div/a[11]').click()


def main():
    #signUp()
    login()
    bookFlight()

main()
time.sleep(50)
print(browser.title)
browser.quit()

