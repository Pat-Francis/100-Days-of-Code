from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from bs4 import BeautifulSoup
import requests

GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")
ZILLOW_URL = os.getenv("ZILLOW_URL")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Accept-Language": "en-US"
}
response = requests.get(url=ZILLOW_URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

property_addresses = [address.get_text() for address in soup.find_all(class_="list-card-addr")]
property_prices = [price.get_text() for price in soup.find_all(class_="list-card-price")]

# TODO fix property_links: Currently gets fulls URLS but not short form (e.g.href="/b/1919-market-oakland-ca-9NThj3/")
property_urls = [url.get('href') for url in soup.find_all(name="a", class_="list-card-link list-card-link-top-margin")]

print(len(property_addresses))
print(len(property_prices))
print(property_urls)
# chrome_driver_path = Service("C:/Dev/chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_driver_path)
# driver.maximize_window()
# driver.get(GOOGLE_FORM_URL)
