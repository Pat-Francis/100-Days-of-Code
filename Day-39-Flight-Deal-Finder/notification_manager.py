import smtplib
import os

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
RECEIVING_EMAIL = os.getenv("RECEIVING_EMAIL")


class NotificationManager:

    def send_email(self, message, emails, google_flight_link):
        email_subject = "Low Price Alert!"
        email_body = message

        # encode the email_body to remove non-ascii characters (non-ascii character '\xa0' caused the email to fail)
        body_encode = email_body.encode("ascii", errors="ignore")
        body_decode = body_encode.decode()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:{email_subject}\n\n{body_decode}\n{google_flight_link}".encode('utf-8')
                    )
