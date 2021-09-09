import requests
import os
from datetime import date
from datetime import timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

today = date.today()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))
get_stock = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
get_stock.raise_for_status()
stock_data = get_stock.json()

yesterday_close_price = float(stock_data["Time Series (Daily)"].get(yesterday).get("4. close"))
day_before_close_price = float(stock_data["Time Series (Daily)"].get(day_before_yesterday).get("4. close"))

print(yesterday_close_price / day_before_close_price * 100)
print(today, type(yesterday), day_before_yesterday)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}
get_news = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
get_news.raise_for_status()
news_data = get_news.json()
latest_news = news_data["articles"][0:3]
news_title = latest_news.get("title")
news_content = latest_news.get("content")


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""