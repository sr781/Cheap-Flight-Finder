from flight_data import FlightData
import requests
from notification_manager import NotificationManager
import os
price_search = FlightData()
twilio_message = NotificationManager()

SHEETY_PRICE_POST = f"https://api.sheety.co/aa130fe99bf6cb9d1fd289fd51d9eef4/flightDealsSulav/prices"

response = requests.get(url=SHEETY_PRICE_POST, auth=("sr781", os.environ["SHEETY_PASSWORD"]))  # This "get" request obtains the desired google sheet data
response_data = response.json()  # The sheet data is parsed into a JSON format


for index in response_data["prices"]:
    fly_to_city = index["city"]  # The destination city name
    fly_to_airport = index["iataCode"]  # The destination airport "iata" code
    flight_data = price_search.price_checker_for_country(index["iataCode"])  # The "iataCode" is used as an argument for the price checker function
    print(f"{index['city']}: £{flight_data[2]}")  # The destination city and price for a flight is printed
    if flight_data[2] <= index["lowestPrice"]:  # If the cost is lower than the specified price in Google sheets, this if statement is triggered
        twilio_message.twilio_message(departed=flight_data[0], returned=flight_data[1], cost=flight_data[2],  # Function to send sms to user is called
                                      fly_from=flight_data[3], fly_to_airport=fly_to_airport, fly_to_city=fly_to_city)