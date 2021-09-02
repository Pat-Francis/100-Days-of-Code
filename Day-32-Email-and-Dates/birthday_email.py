# Extra Hard Starting Project #
import datetime as dt
import smtplib
import random
import pandas as pd

# Load CSV into Pandas Dataframe
data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
today_month = now.month
today_day = now.day

for index, row in data.iterrows():
    if today_day == row["day"] and today_month == row["month"]:
        # Open a random letter
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            # Read the txt and replace the [NAME] placeholder with the persons name
            contents = letter.read().replace("[NAME]", row["name"])

            my_email = "email@gmail.com"
            my_password = "password1234"
            receiving_email = row["email"]

            # Send email using contents for the email body
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=receiving_email,
                                    msg=f"Subject:Happy Birthday!!\n\n{contents}"
                                    )
