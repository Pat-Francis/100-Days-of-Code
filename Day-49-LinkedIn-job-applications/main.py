from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

linkedin_username = os.getenv("LINKEDIN_USERNAME")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")

chrome_driver_path = Service("C:/Dev/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

enter_username = driver.find_element(By.ID, "username")
enter_username.send_keys(linkedin_username)

enter_password = driver.find_element(By.ID, "password")
enter_password.send_keys(linkedin_password)
enter_password.send_keys(Keys.ENTER)
time.sleep(5)

element_class_name = "jobs-search-results__list-item"
jobs = driver.find_elements(By.CLASS_NAME, element_class_name)

for index in range(len(jobs)):
    # Refresh jobs every iteration - otherwise throws StaleElementReferenceException as items are no longer in
    # Document Object Model (DOM).  DOM changes every interaction with web page?
    jobs = driver.find_elements(By.CLASS_NAME, element_class_name)

    jobs[index].click()
    time.sleep(3)

    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()

driver.quit()
