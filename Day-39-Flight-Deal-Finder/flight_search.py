import os
import requests
from flight_data import FlightData

KIWI_LOC_URL = os.getenv("KIWI_LOC_URL")
KIWI_FLIGHT_URL = os.getenv("KIWI_FLIGHT_URL")
KIWI_KEY = os.getenv("KIWI_KEY")


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def get_destination_iata_code(self, city_name):
        headers = {
            "apikey": KIWI_KEY,
            "accept": "application/json",
        }
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=KIWI_LOC_URL, headers=headers, params=query)
        results = response.json()["locations"]
        city_code = results[0]["code"]
        return city_code

    def check_flights(self, origin_city_code, destination_city_code, time_from, time_to):
        headers = {"apikey": KIWI_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": time_from.strftime("%d/%m/%Y"),
            "date_to": time_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=KIWI_FLIGHT_URL, headers=headers, params=query)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                go_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
