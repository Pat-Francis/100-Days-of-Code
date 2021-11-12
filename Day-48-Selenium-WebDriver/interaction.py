from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:/Dev/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number_of_articles = driver.find_element(By.XPATH, "//a[@title='Special:Statistics']")
number_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(number_of_articles.text)

driver.quit()
