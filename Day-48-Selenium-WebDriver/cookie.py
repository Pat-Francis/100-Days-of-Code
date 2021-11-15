from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C:/Dev/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

long_time_end = time.time() + 300  # 5 minute time loop

while time.time() < long_time_end:
    short_time_end = time.time() + 5  # 5 second time loop
    while time.time() < short_time_end:
        cookie.click()
    available_upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")

    for i in range(len(available_upgrades) - 1, 0, -1):
        try:
            available_upgrades[i].click()
        # TODO Fix bare except (research and implement Selenium exception(s))
        except:
            pass

cps = driver.find_element(By.CSS_SELECTOR, "#cps")
cookies_count = driver.find_element(By.ID, "money")
print(f"Cookies per second: {cps.text}.  {cookies_count.text} in total.")

driver.quit()
