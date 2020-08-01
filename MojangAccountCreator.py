# MojangAccountCreator.py

# Copyright (C) Shad0w7, Kiriyn - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Shad0w7 <shad0wasdfseven@gmail.com>, August 2020


# -- Dependencies -- 

import selenium # Selenium
from selenium import webdriver # Chrome Webdrivers
from selenium.webdriver.support.ui import Select # Select Framework
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import string
import random
from random import randint # For Date Generation
import time
from selenium.webdriver.common.keys import Keys
from datetime import date # Current Date
from fake_useragent import UserAgent
from dotenv import load_dotenv
import os

# OS.GETENV in progress

VERSION = "InDev0.0"
PATH_TO_DRIVERS = "/Users/ayushnayak/Downloads/" # Definitely one for the .env
MOJANG_URL = "https://my.minecraft.net/en-us/store/minecraft/#register"
TEMP_MAIL_URL = "https://temp-mail.org/en/"
CREDITS = "Created by Shad0w7, Moral Support by Kiriyn"
PROXY = "199.195.248.24:8080"

# -- Drivers --      

Verbose = True
if Verbose:
    print('Starting in Verbose Mode:')
currentDriver = 'chromedriverASD' # chromium, chromiumASD = AntiSeleniumDetection (modified executable)

# -- XPaths -- 

# Note: XPath Names MAY CHANGE WITHOUT WARNING!!!!!

# Mojang Filler Website

emailXPath = '//*[@name="email"]'
emailRepeatXPath = '//*[@name="repeatEmail"]'
passwordXPath = '//*[@name="password"]'
createAccountXPath = '//*[@id="orderflow"]/div[2]/div/div/form/div[6]/button'
dayXPath = '//*[@name="day"]'
monthXPath = '//*[@name="month"]'
yearXPath = '//*[@name="year"]'

# Mojang Verify Website

verificationCodeXPath = '//*[@name="token"]'
verifyButtonXPath = '//*[@id="orderflow"]/div[2]/div/div/form/div/div[2]/button'

# Temp-Mail

emailDisplayXPath = '//*[@id="mail"]'
refrestButtonXPath = '//*[@id="click-to-refresh"]'
HREFEmailXPath = '/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a'
emailCodeXPath = '/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[2]/div[3]/div/p[4]'


# -- Generate Values to Send --

# Date

dayValue = str(random.randint(1, 27)) # Day

monthValue = str(random.randint(1, 12)) # Month

yearValue = str(random.randint(1975, 2001)) # Year

# Password

from random import *
characters = string.ascii_letters + string.digits
passcode =  "".join(choice(characters) for x in range(randint(8, 16)))

if Verbose:
    print('MojangAccountSpammer Version: {0} \n{1}'.format(VERSION, CREDITS))
    print("----------------")
if Verbose:
    print('Current Path: {0} \nCurrent Browser: {1}'.format(str(PATH_TO_DRIVERS), currentDriver))
    print('Session Passcode: {0}'.format(passcode))
    print('Session Date: {0}/{1}/{2}'.format(monthValue, dayValue, yearValue))



# -- Setting up the WebDriver to Look like a Real Request--

# NOTE: Google's reCaptcha v2 Invisible, detects that Selenium is being used, and serves a reCaptcha without an audio option, which we need

# Proxy

# Proxies are not a good idea, as they slow down the internet


# Options

options = webdriver.ChromeOptions()

#options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument('start-maximized')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

# Path

path = str(PATH_TO_DRIVERS) + currentDriver
driver = webdriver.Chrome(options=options, executable_path=path)

# Scripts

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

if Verbose:
    print('Session User Agent: {}'.format(driver.execute_script("return navigator.userAgent;")))

# Open the second window

driver.get("https://www.google.com")
parentGUID = driver.current_window_handle

# open a link in a new window
actions = ActionChains(driver)
about = driver.find_element_by_link_text('About')
actions.key_down(Keys.COMMAND).click(about).key_up(Keys.COMMAND).perform()

driver.switch_to.window(driver.window_handles[-1])

# Open Temp-Mail Website

driver.get(TEMP_MAIL_URL)


# -- Gather Email Address --

childGUID = driver.current_window_handle

while(True): # Make sure its not tempmails stupid "Loading..." thing
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

if Verbose: 
    print('Email Gathered!')
    print('Session Email: {}'.format(x.get_attribute('value')))
    print('Switching to minecraft.net')


# -- Inputting Data to minecraft.net --


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

# -- Solve Captcha --

# Note: in the future, there should be an automated captcha solver

driver.find_element_by_xpath(createAccountXPath).click()

# Now everything has been sent and reCAPCHA should show up

while True:
    time.sleep(1)
    if (str(driver.current_url) == 'https://my.minecraft.net/en-us/store/minecraft/#register'):
        continue
    break


if Verbose:
    print('Switching to temp-mail')
driver.switch_to.window(childGUID)

# On TempMail Website


# -- Gather Code from Email --

driver.find_element_by_xpath(refrestButtonXPath).click()

if Verbose:
    print('Waiting for email...')
while True:
    time.sleep(1)
    try:
        mojangEmailLink = driver.find_element_by_xpath(HREFEmailXPath).get_attribute('href')
        break
    except:
        continue
if Verbose:
    print('Link Found! {}'.format(mojangEmailLink))

driver.get(mojangEmailLink)

while True:
    time.sleep(1)
    try:
        element = driver.find_element_by_xpath(emailCodeXPath)
        break
    except:
        input('Enter to Retry!')
        continue
    

code = '{}'.format(element.get_attribute('innerHTML'))

x = code.replace(' ', '')
z = x.strip()
if Verbose:
    print('Code: {}'.format(z))

time.sleep(0.1)
if Verbose:
    print('Switching to minecraft.net')

# Back to minecraft.net
driver.switch_to.window(parentGUID)

# -- Enter Code into minecraft.net --

driver.find_element_by_xpath(verificationCodeXPath).send_keys(z)
driver.find_element_by_xpath(verifyButtonXPath).click()

# Post Data

'''
Format:
<EMAIL>_<PASSWORD>_<DATE>_<CREATIONDATE>_<MC>
ex:
boyoh96857@ascaz.net_DUmOfbUG4hmJcLt_2/23/1978_7/30/2020_FALSE

'''
dateString = '{0}/{1}/{2}'.format(monthValue, dayValue, yearValue)
postString = '{0}_{1}_{2}_{3}_{4}'.format(emailValue, passcode, dateString, date.today(), 'FALSE')
if Verbose:
    print('Appending...')
f = open("list.txt", 'a')
f.write('\n')
f.write(postString)
f.close()

if Verbose:
    print('Appended Text!')

# Ready to Quit !

# input('Program Finished! \nPress Enter to Quit. . . ') # Uncomment if you want control over what happens after a successful account creation
if Verbose:
    print('Quitting. . .')
driver.quit()