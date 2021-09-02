import datetime as dt
import smtplib
import random

# Open quotes.txt
with open("quotes.txt") as quotes_file:
    quote_list = quotes_file.readlines()

day_of_week = dt.datetime.now().weekday()

# If day of the week is Thursday
if day_of_week == 3:
    quote_to_send = random.choice(quote_list)

    my_email = "email@gmail.com"
    password = "password1234"
    # Open email connection and send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Weekly Motivation\n\n{quote_to_send}"
        )
