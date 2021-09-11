import requests
import datetime
import os

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# # Create new user https://pixe.la/@luminaries
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Time Coding",
#     "unit": "minutes",
#     "type": "int",
#     "color": "momiji",
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# # requests.post() update to graph1
# post_data = {
#     "date": date_today.strftime("%Y%m%d"),
#     "quantity": "100",
# }
# date_today = datetime.date.today()
#
# post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# response = requests.post(url=post_endpoint, json=post_data, headers=headers)
# print(response.text)

# # request.put() to previous date
# day_to_update = "20210910"
#
# put_data = {
#     "quantity": "45"
# }
#
# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_to_update}"
# response = requests.put(url=put_endpoint, json=put_data, headers=headers)
# print(response.text)

# request.delete() a previous date
day_to_delete = "20210910"

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_to_delete}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
