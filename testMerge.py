# testMerge.py

# Copyright (C) Ayush Nayak, Daniel Deng - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Ayush Nayak <shad0wasdfseven@gmail.com>, August 2020


# -- Dependencies -- 

from generateEmail import * # Generate Email
import selenium # Selenium
from selenium import webdriver # Chrome Webdrivers
from selenium.webdriver.support.ui import Select # Select Framework
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import string
import random
from random import randint # For Date
import time
from selenium.webdriver.common.keys import Keys

# OS.GETENV in progress

VERSION = "InDev0.0"
PATH_TO_DRIVERS = "/Users/ayushnayak/Downloads/"
MOJANG_URL = "https://my.minecraft.net/en-us/store/minecraft/#register"
TEMP_MAIL_URL = "https://temp-mail.org/en/"


# -- Drivers --      

Verbose = True
if Verbose:
    print('Starting in Verbose Mode:')
pathToChrome = PATH_TO_DRIVERS
currentDriver = 'chromium' # chrome, gecko (mozilla)

# -- XPaths -- 

# Note: XPath Names MAY CHANGE WITHOUT WARNING!!!!!

# Mojang

emailXPath = '//*[@name="email"]'

emailRepeatXPath = '//*[@name="repeatEmail"]'

passwordXPath = '//*[@name="password"]'

createAccountXPath = '//*[@id="orderflow"]/div[2]/div/div/form/div[6]/button'

dayXPath = '//*[@name="day"]'

monthXPath = '//*[@name="month"]'

yearXPath = '//*[@name="year"]'


# Temp-Mail

emailDisplayXPath = '//*[@id="mail"]'

refrestButtonXPath = '//*[@id="click-to-refresh"]'

firstEmailXPath = '/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a'

# -- Generate Values to Send --

# Email

email = 'NOTSETYET@NO.COM' # Retrieve this from a Temp Mail Microservice (Static for now)


# Day

dayValue = str(random.randint(1, 27))

# Month

monthValue = str(random.randint(1, 12))

# Year

yearValue = str(random.randint(1975, 2001))

# Password

from random import *
characters = string.ascii_letters + string.digits
passcode =  "".join(choice(characters) for x in range(randint(8, 16)))



print('MojangAccountSpammer Version: {} \nCreated by Shad0w7 and Kiriyn'.format(VERSION))
print("----------------")
if Verbose:
    print('Current Path: {0} \nCurrent Browser: {1}'.format(pathToChrome, currentDriver))
    print('Session Passcode: {0}'.format(passcode))
    print('Session Date: {0}/{1}/{2}'.format(monthValue, dayValue, yearValue))



# Setting up Chrome
if currentDriver == 'chromium':
    driver = webdriver.Chrome(pathToChrome + 'chromedriver')

#open the second window





driver.get("https://www.google.com")
parentGUID = driver.current_window_handle

# open a link in a new window
actions = ActionChains(driver)
about = driver.find_element_by_link_text('About')
actions.key_down(Keys.COMMAND).click(about).key_up(Keys.COMMAND).perform()

driver.switch_to.window(driver.window_handles[-1])


driver.get(TEMP_MAIL_URL)

childGUID = driver.current_window_handle

while(True):
    time.sleep(0.5)
    test = driver.find_element_by_xpath(emailDisplayXPath)
    if test.get_attribute('value') == 'Loading':
        continue
    if test.get_attribute('value') == 'Loading.':
        continue
    if test.get_attribute('value') == 'Loading..':
        continue
    if test.get_attribute('value') == 'Loading...':
        continue
    break

x = driver.find_element_by_xpath(emailDisplayXPath)

print('Session Email: {}'.format(x.get_attribute('value')))

emailValue = '{}'.format(x.get_attribute('value'))

driver.switch_to.window(parentGUID)

driver.get(MOJANG_URL)

while True:
    try:
        driver.find_element_by_xpath(emailXPath).send_keys(emailValue)
        break
    except:
        continue

driver.find_element_by_xpath(emailRepeatXPath).send_keys(emailValue)
driver.find_element_by_xpath(passwordXPath).send_keys(passcode)

daySelector = Select(driver.find_element_by_xpath(dayXPath))
monthSelector = Select(driver.find_element_by_xpath(monthXPath))
yearSelector = Select(driver.find_element_by_xpath(yearXPath))

daySelector.select_by_value(dayValue)
monthSelector.select_by_value(monthValue)
yearSelector.select_by_value(yearValue)

driver.find_element_by_xpath(createAccountXPath).click()

# Now everything has been sent and reCAPCHA should show up

input('Enter once ReCAPTCHA Completed: ')

driver.switch_to.window(childGUID)

# On TempMail Website

driver.find_element_by_xpath(refrestButtonXPath).click()

input('Enter Once New Email: ')
try:
    mojangEmailLink = driver.find_element_by_xpath(firstEmailXPath).get_attribute('href')
    print(mojangEmailLink)
except:
    print('FAILED')
    input()
    driver.quit()

input('Enter to Quit: ')
driver.quit()