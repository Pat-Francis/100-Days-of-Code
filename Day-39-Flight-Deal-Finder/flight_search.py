import os
import requests

KIWI_LOC_URL = os.getenv("KIWI_LOC_URL")
KIWI_KEY = os.getenv("KIWI_KEY")

headers = {
    "apikey": KIWI_KEY,
    "accept": "application/json",
}


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def __init__(self):
        self.response = requests.get(url=KIWI_LOC_URL)

    def get_iata_code(self, city):

        parameters = {
            "term": city,
            "location_types": "city",
            "limit": 1,
        }

        self.response = requests.get(url=KIWI_LOC_URL, params=parameters, headers=headers)
        self.response.raise_for_status()
        return self.response.json()["locations"][0].get("code")
