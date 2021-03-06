from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from bs4 import BeautifulSoup

GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")
ZILLOW_URL = os.getenv("ZILLOW_URL")

chrome_driver_path = Service("C:/Dev/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()
driver.get(ZILLOW_URL)
time.sleep(5)

# Tab to the 'Rental Listings' panel
for _ in range(20):
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()

# scroll to the bottom to load 40 properties (instead of the default 9)
for _ in range(140):
    webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()

time.sleep(5)

page_html = driver.page_source
soup = BeautifulSoup(page_html, "html.parser")

property_addresses = [address.get_text() for address in soup.find_all(class_="list-card-addr")]
property_prices = [price.get_text() for price in soup.find_all(class_="list-card-price")]
property_urls = [url.get('href') for url in soup.find_all(name="a", class_="list-card-link", tabindex='0')]

# update all short urls to full length
# e.g '/b/22-margrave-pl-san-francisco-ca-9NLzZs/' -> 'https://www.zillow.com/b/22-margrave-pl-san-francisco-ca-9NLzZs/
url_prefix = "https://www.zillow.com"

for url in range(len(property_urls)):
    if not property_urls[url].startswith("https"):
        property_urls[url] = f"{url_prefix}{property_urls[url]}"

driver.get(GOOGLE_FORM_URL)
time.sleep(3)

for i in range(len(property_addresses)):
    form_text_boxes = driver.find_elements(By.CLASS_NAME, "quantumWizTextinputPaperinputInput")
    submit_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Submit')]")

    form_text_boxes[0].send_keys("", property_addresses[i])
    form_text_boxes[1].send_keys("", property_prices[i])
    form_text_boxes[2].send_keys("", property_urls[i])
    submit_button.click()

    submit_another_link = driver.find_element(By.LINK_TEXT, "Submit another response")
    submit_another_link.click()

driver.quit()
