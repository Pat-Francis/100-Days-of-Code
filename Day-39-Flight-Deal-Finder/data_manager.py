import os
import requests

SHEET_URL = os.getenv("SHEET_URL")
SHEET_KEY = os.getenv("SHEET_KEY")
SHEET_CUSTOMERS = os.getenv("SHEET_CUSTOMERS")


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_URL)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_URL}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEET_CUSTOMERS)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
