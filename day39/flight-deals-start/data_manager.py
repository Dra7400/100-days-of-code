import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ce33c06ed6227d004580b7b91266772e/flightDeals/prices"
TOKEN = "Lone7400!"


class DataManager:
    def __init__(self):
        self.destination = {}

    def get_destination(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination = data["prices"]
        return self.destination

    def update_destination(self):
        for city in self.destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
