import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:/SeleniumDrivers"
testingWebpage = "https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html"

# you should download chromedriver and put it in the same directory as this file
# https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.43/
os.environ["PATH"] += os.pathsep + path
driver = webdriver.Chrome()

# open the website
driver.get(testingWebpage)
driver.implicitly_wait(10)

# find the download button
downloadBtn = driver.find_element_by_id("downloadButton")
downloadBtn.click()

#  get progress element after it is completed
WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element(
    (By.CLASS_NAME, "progress-label"), "Complete!")
)
