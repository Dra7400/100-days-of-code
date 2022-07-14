from twilio.rest import Client

TWILIO_SID = "AC2b4059c353150ccf8f7b23cfc91592a8"
TWILIO_AUTH_TOKEN = "b68f661217562ef9af3ceb6c3dfb88a1"
TWILIO_VIRTUAL_NUMBER = "(970) 687-7855"
TWILIO_VERIFIED_NUMBER = "(662) 671-0470"


class NotificationManager:

    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
