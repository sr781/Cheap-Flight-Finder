import os

from twilio.rest import Client
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]


class NotificationManager:  # This class is responsible for sending the text message via Twilio

    def twilio_message(self, departed, returned, cost,  fly_from, fly_to_city, fly_to_airport):
        text_message = f"\n Alert! A low price flight from London-{fly_from} to {fly_to_city}-{fly_to_airport}," \
                       f" from {departed} to {returned} is available from only £{cost}"  # The message sent if a cheap flight is found
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)  # This section is used to send the data via Twilio
        message = client.messages \
            .create(
            body=text_message,  # The message was created earlier and stored in the "text_message" variable
            from_='+13023376284',  # The host phone number from where it is sent
            to='+4407565211105'  # The recipient phone number from where it will be sent
        )
        print(f"Cheap flight for {fly_to_city} found! Sending SMS...")

