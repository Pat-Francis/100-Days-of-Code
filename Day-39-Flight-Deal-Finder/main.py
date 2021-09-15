from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()

for row in data_manager.sheet_data["prices"]:
    if row["iataCode"] == "":
        # get iata code based on city name
        city_code = flight_search.get_iata_code(row["city"])
        row["iataCode"] = city_code

data_manager.update_iata_code()
