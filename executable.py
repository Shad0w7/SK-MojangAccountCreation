# executable.py

# Copyright (C) Shad0w7, Kiriyn - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Shad0w7 <shad0wasdfseven@gmail.com>, August 2020

# -- Imports --

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

def MAC():
    input('Press enter when you are ready to start creating the accounts. . .')
    os.system('python MojangAccountCreator.py')


def loadFiles():
    input('Please input a file named "list.txt" into the folder "Drop_txt_Here" and press enter. . .')
    while True:
        try:
            file1 = open('Drop_txt_Here/list.txt', 'r')
        except:
            input('File not found or unreadable! (Make sure to rename your file "list.txt"!) Ctrl-C to quit! Enter to try again. . .')
            continue
        break
    print('File Found! Reading. . .')
    try:
        lines = file1.readlines()
    except:
        print('File Unreadable! Exiting. . .')
        loadFiles()
    correct = 0
    file2 = open('list.txt', 'a')
    file2.write('\n')
    for x in lines:
        if len(x.split('_')) != 5:
            print('[ERROR]: {} is in the wrong format, not appending! Format: <EMAIL>_<PASSWORD>_<DATE>_<CREATIONDATE>_<MC>'.format(x))
            continue
        else:
            file2.write('{}'.format(x))
            correct += 1
    print('\nCompleted for {} lines!'.format(correct))

   
    file1.close()
    


def snipe():
    print('Still unfinished for now - sorry!')

print('Welcome to the Kiriyn Shad0w Sniper! The Sniper is still InDev and does not work fully right now!\n')

print('1. Mojang Account Creation [Alpha] \n2. Load Accounts [Unfinished] \n3. Snipe Accounts [Unfinished] \n4. to quit')
while True:
    x = input('> ')
    if x != '1' and x != '2' and x != '3' and x != '4' and x != '':
        print('Please input either "1", "2", "3" or "4"')
        continue
    
    if x == '':
        continue

    if x == '4':
        exit()

    if x == '1':
        MAC()
        continue

    if x == '2':
        loadFiles()
        continue

    if x == '3':
        snipe()
        continue

        
    