from twilio.rest import Client

TWILIO_SID = "AC2b4059c353150ccf8f7b23cfc91592a8"
TWILIO_AUTH_TOKEN = "b68f661217562ef9af3ceb6c3dfb88a1"
TWILIO_VIRTUAL_NUMBER = "(970) 687-7855"
TWILIO_VERIFIED_NUMBER = "(662) 671-0470"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "david.r.adams@gmail.com"
MY_PASSWORD = "logan7400"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(YOUR_EMAIL_PROVIDER_EMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode(
                        'utf-8')
                )
