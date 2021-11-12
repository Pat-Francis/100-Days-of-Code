from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("C:/Dev/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # number_of_articles = driver.find_element(By.XPATH, "//a[@title='Special:Statistics']")
# number_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(number_of_articles.text)
# # number_of_articles.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Pat")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Francis")

email = driver.find_element(By.NAME, "email")
email.send_keys("pfrancis@myemail.com")

submit_button = driver.find_element(By.CSS_SELECTOR, "form button")
submit_button.submit()

# driver.quit()
