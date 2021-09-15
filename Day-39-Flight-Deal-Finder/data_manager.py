import os
import requests

SHEET_URL = os.getenv("SHEET_URL")
SHEET_KEY = os.getenv("SHEET_KEY")


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):

        self.response = requests.get(url=SHEET_URL)
        self.sheet_data = self.response.json()
        self.sheet_headers = {
            "Authorization": f"Bearer {SHEET_KEY}",
            "Content-Type": "application/json"
        }

    def update_iata_code(self):
        for row in self.sheet_data["prices"]:
            new_data = {
                "price": {
                    "id": row["id"],
                    "iataCode": row["iataCode"]
                }
            }
            sheet_response = requests.put(url=f"{SHEET_URL}/{row['id']}", json=new_data, headers=self.sheet_headers)
            print(sheet_response.text)
