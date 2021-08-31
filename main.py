import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = r"C:/SeleniumDrivers"
testingWebpage = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"

# you should download chromedriver and put it in the same directory as this file
# https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.43/
os.environ["PATH"] += os.pathsep + path
driver = webdriver.Chrome()

# open the website
driver.get(testingWebpage)
driver.implicitly_wait(5)

# close the ads
try:
    no_button = driver.find_element_by_class_name("at-cm-no-button")
    no_button.click()
except:
    print("No ads found, skipping ...")

# find sum buttons
sum1 = driver.find_element_by_id("sum1")
sum2 = driver.find_element_by_id("sum2")

# enter the numbers using the keys
sum1.send_keys(Keys.NUMPAD1 + Keys.NUMPAD4)
sum2.send_keys(Keys.NUMPAD1 + Keys.NUMPAD4)

# get the submit numbers button

btn = driver.find_element_by_css_selector('button[onClick="return total()"]')
btn.click()
