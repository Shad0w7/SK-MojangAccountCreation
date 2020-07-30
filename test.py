# test.py

# Copyright (C) Ayush Nayak, Daniel Deng - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Ayush Nayak <shad0wasdfseven@gmail.com>, August 2020


# -- Dependencies -- 

from generateEmail import * # Generate Email
import selenium # Selenium
from selenium import webdriver # Chrome Webdrivers
from selenium.webdriver.support.ui import Select # Select Framework
import string
import random
from random import randint # For Date
import time

# OS.GETENV in progress

VERSION = "InDev0.0"
PATH_TO_DRIVERS = "/Users/ayushnayak/Downloads/"
MOJANG_URL = "https://my.minecraft.net/en-us/store/minecraft/#register"

# -- Drivers --      

Verbose = True
if Verbose:
    print('Starting in Verbose Mode:')
pathToChrome = PATH_TO_DRIVERS
currentDriver = 'chrome' # chrome, gecko (mozilla)
currentMojangRegisterURL = MOJANG_URL

# -- XPaths -- 

# Note: XPath Names MAY CHANGE WITHOUT WARNING!!!!!

emailXPath = '//*[@name="email"]'

emailRepeatXPath = '//*[@name="repeatEmail"]'

passwordXPath = '//*[@name="password"]'

createAccountXPath = '//*[@id="orderflow"]/div[2]/div/div/form/div[6]/button'

dayXPath = '//*[@name="day"]'

monthXPath = '//*[@name="month"]'

yearXPath = '//*[@name="year"]'



# -- Generate Values to Send --

# Email

email = 'asdf@asdf.com' # Retrieve this from a Temp Mail Microservice (Static for now)


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

print("----------------\n")

print('MojangAccountSpammer Version: {} \nCreated by Shad0w7 and Kiriyn'.format(VERSION))
if Verbose:
    print('Current Path: {0} \nCurrent Browser: {1}'.format(pathToChrome, currentDriver))
    print('Session Email: {0} \nSession Passcode: {1}'.format(email, passcode))
    print('Session Date: {0}/{1}/{2}'.format(dayValue, monthValue, yearValue))



# Setting up Chrome
if currentDriver == 'chrome':
    driver = webdriver.Chrome(pathToChrome + 'chromedriver')

# Only use the above to test if Selenium is working on your machine!

driver.get(currentMojangRegisterURL)
time.sleep(0.7)

driver.find_element_by_xpath(emailXPath).send_keys(email)
driver.find_element_by_xpath(emailRepeatXPath).send_keys(email)
driver.find_element_by_xpath(passwordXPath).send_keys(passcode)

daySelector = Select(driver.find_element_by_xpath(dayXPath))
monthSelector = Select(driver.find_element_by_xpath(monthXPath))
yearSelector = Select(driver.find_element_by_xpath(yearXPath))

daySelector.select_by_value(dayValue)
monthSelector.select_by_value(monthValue)
yearSelector.select_by_value(yearValue)

driver.find_element_by_xpath(createAccountXPath).click() #EXPERIMENTAL
# Now everything has been selected