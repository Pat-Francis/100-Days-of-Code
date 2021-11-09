import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
pp = pprint.PrettyPrinter(indent=4)

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

BASE_URL = "https://www.billboard.com/charts/hot-100/"
chosen_date = input("Please input the date you would like (YYYY-MM-DD):")
URL = f"{BASE_URL}{chosen_date}"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Find all the HTML elements that contain the song names
all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

# Pull song names from all_songs and store in a list
song_titles = [song.getText() for song in all_songs]

# Set scope for spotify access token
scope = "playlist-modify-private"

# Auth with Spotify, adds the .cache file to the directory which holds the Spotify access token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# Pull user info from Spotify and print current users display id
user_info = sp.current_user()
print(user_info.get("id"))

song_URIs = []
year = chosen_date.split("-")[0]
# Iterate through the list of song titles and get the corresponding Spotify track URI, if the track exists
for song in song_titles:
    search_result = sp.search(q=f"track: {song} year: {year}", type="track")

    try:
        uri = search_result["tracks"]["items"][0]["uri"]
        song_URIs.append(uri)
    except IndexError:
        print(f"Could not find '{song}' on Spotify.  Skipped.")

pp.pprint(song_URIs)
