# tempMailDelegate.py

# Copyright (C) Ayush Nayak, Daniel Deng - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Ayush Nayak <shad0wasdfseven@gmail.com>, August 2020


# -- Dependencies -- 

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
TEMP_MAIL_URL = "https://temp-mail.org/en/"

Verbose = True
if Verbose:
    print('Starting in Verbose Mode:')
pathToChrome = PATH_TO_DRIVERS
currentDriver = 'chrome' # chrome, gecko (mozilla)

# -- XPaths -- 

# Note: XPath Names MAY CHANGE WITHOUT WARNING!!!!!

emailDisplayXPath = '//*[@id="mail"]'

refrestButtonXPath = '//*[@id="click-to-refresh"]'

# -- Get Email --

if currentDriver == 'chrome':
    driver = webdriver.Chrome(pathToChrome + 'chromedriver')

driver.get(TEMP_MAIL_URL)

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

input('Enter to Quit: ')
driver.quit()
