import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.billboard.com/charts/hot-100/"
chosen_date = input("Please input the date you would like (YYYY-MM-DD):")
URL = f"{BASE_URL}{chosen_date}"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Find all the HTML elements that hold the song names
all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

# Pull song names from all_songs and store in a list
song_titles = [song.getText() for song in all_songs]


