from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_IATA_CODE = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_iata_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_IATA_CODE,
        destination["iataCode"],
        time_from=tomorrow,
        time_to=six_month_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_email(
            f"Only GBP {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to " \
            f"{flight.destination_city}-{flight.destination_airport} from {flight.go_date} to {flight.return_date}."
        )
