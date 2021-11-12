from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:/Dev/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# Maximise window to grab full dates.  Smaller window only returns day and month (not year).
driver.maximize_window()
driver.get("https://www.python.org")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events_dict = {}
for i in range(0, len(event_times)):
    events_dict[i] = {"time": event_times[i].text, "name": event_names[i].text}
print(events_dict)

driver.quit()
