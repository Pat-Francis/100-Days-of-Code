import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
open_trivia_response = requests.get(url="https://opentdb.com/api.php", params=parameters)
open_trivia_response.raise_for_status()
open_trivia_data = open_trivia_response.json()

question_data = open_trivia_data["results"]
