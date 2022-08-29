from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests
import os
headers = {
    "apikey": os.environ["flight_api_key"],
}
PRICE_POST = "https://tequila-api.kiwi.com/v2/search"


class FlightData:

    def price_checker_for_country(self, fly_to):  # This functions role is to find flights from tommorow to six months from now
        now = datetime.now()

        tommorow_date = now + relativedelta(days=1)  # The "relativedelta" function is used to represent an interval of time
        tommorow_date = tommorow_date.strftime("%d/%m/%Y")  # The date is formatted for the API parameter
        six_month_date = now + relativedelta(months=6)
        six_month_date = six_month_date.strftime("%d/%m/%Y")

        sheety_price_params = {  # The parameters for the flight, with a minimum stay of 3 days and maximum of 28
            "fly_from": "LON",
            "fly_to": fly_to,  # The destination is obtained from the argument
            "date_from": tommorow_date,
            "date_to": six_month_date,
            "curr": "GBP",
            "flight_type": "round",
            "nights_in_dst_from": "3",
            "nights_in_dst_to": "28"
        }

        try:
            cheap_response = requests.get(url=PRICE_POST, headers=headers, params=sheety_price_params)  # The "get" request is used to obtain the information
            cheap_response_data = cheap_response.json()  # Data is parsed into a JSON format
            return self.time_seperate(cheap_response_data["data"][0]["route"][0]["local_departure"]), \
                   self.time_seperate(cheap_response_data["data"][0]["route"][1]["local_departure"]), \
                   cheap_response_data["data"][0]["price"], cheap_response_data["data"][0]["flyFrom"]
            #  The departure from home country, departure from host country and price is returned as a tuple
        except IndexError:
            print(f"No flights found for {fly_to}")
    def time_seperate(self, time):  # This function splits the date into the desired format
        split_time = time.split("T")
        return split_time[0]
