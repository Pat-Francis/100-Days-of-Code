from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

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

# driver.quit()
