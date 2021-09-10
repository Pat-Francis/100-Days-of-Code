import requests
import os
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Get email constants from environment variables
MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVING_EMAIL = os.getenv("RECEIVING_EMAIL")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

# Retrieve the stock data JSON and get the daily time series
get_stock = requests.get(url=ALPHA_ENDPOINT, params=stock_parameters)
get_stock.raise_for_status()
stock_data = get_stock.json()["Time Series (Daily)"]

# Take the stock_data dict and add the values to a list
stock_data_list = [value for (key, value) in stock_data.items()]

# Get the stock close price from the two most recent days
yesterday_close_price = float(stock_data_list[0]["4. close"])
day_before_close_price = float(stock_data_list[1]["4. close"])

percent_change = round((yesterday_close_price / day_before_close_price * 100) - 100, 2)

if percent_change >= 5 or percent_change <= -5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    # Retrieve the news JSON and grab the latest three articles
    get_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    get_news.raise_for_status()
    news_data = get_news.json()["articles"]
    latest_three_articles = news_data[:3]

    # Set the email subject and body strings
    email_subject = f"{STOCK} {percent_change}%"

    # Add articles headline, brief and URL to the email_body
    email_body = ""
    formatted_body = [f"Headline: {article['title']}\nBrief: {article['description']}\n{article['url']}\n\n"
                      for article in latest_three_articles]

    for article in formatted_body:
        email_body += article

    # encode the email_body to remove non-ascii characters (non-ascii character '\xa0' caused the email send to fail)
    body_encode = email_body.encode("ascii", errors="ignore")
    body_decode = body_encode.decode()

    # Send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECEIVING_EMAIL,
                            msg=f"Subject:{email_subject}\n\n{body_decode}"
                            )
