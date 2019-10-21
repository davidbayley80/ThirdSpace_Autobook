import os
import time
import credentials

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/davidbayley/PycharmProjects/ThirdSpace_Autobook/chromedriver")

browser = webdriver.Chrome(executable_path = DRIVER_BIN)
browser.get('https://www.thirdspace.london/login/')

usernameStr = credentials.username
passwordStr = credentials.password

username = browser.find_element_by_name('email')
username.send_keys(usernameStr)
password = browser.find_element_by_name('password')
password.send_keys(passwordStr)
nextButton = browser.find_element_by_xpath('/html/body/main/article/div/form/div[3]')
nextButton.click()
try:
    element = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/nav/div[1]/div/ul/li[10]/ul/li[1]'))
    )
finally:
    browser.find_element_by_xpath('/html/body/nav/div[1]/div/ul/li[10]/ul/li[1]').click()
    browser.get('https://www.thirdspace.london/timetable/')
    time.sleep(5)
    browser.find_element_by_class_name('fkl-clear').click()
    try:
        element = WebDriverWait(browser, 120).until(
            EC.visibility_of_element_located((By.XPATH,'/html/body/main/div[5]/div/div[2]/div[1]/div/div[3]/div/div[24]'))
        )
    finally:
        browser.find_element_by_xpath('html/body/main/div[5]/div/div[2]/div[1]/div/div[3]/div/div[24]').click()

    try:
        element = WebDriverWait(browser, 120).until(
        EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/input'))
    )
    finally:
        browser.find_element_by_xpath('/html/body/div[2]/div/input').click()