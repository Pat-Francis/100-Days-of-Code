import os
from bs4 import BeautifulSoup
import smtplib
import requests

URL = "https://www.amazon.co.uk/LEGO-92176-LEGO-92176-Ideas-NASA-Apollo-Saturn-V-Space-Rocket-and-Vehicles-Spaceship-Collectors-Building-Set-with-Display-Stand/dp/B08GNXNPR6/ref=sr_1_1?keywords=lego+saturn+v&qid=1636645994&qsid=261-3031590-4329561&sr=8-1&sres=B08GNXNPR6%2CB06XRXB92G%2CB0946LC47L%2CB09C1VGC2J%2CB093KPHXZM%2CB098SHHSR8%2CB09JG1V6C7%2CB0962XV4B9%2CB09HKCN18T%2CB096XMZ6B9%2CB08G1PMDDM%2CB08S3QFHR9%2CB091CLZYQS%2CB0002HLCP8%2CB09JC2RBSN%2CB08TWCR5VT%2CB0992BJJX3%2CB07TB87JKY%2CB083Z7F7CY%2CB07TG91HGB&srpt=TOY_BUILDING_BLOCK"
BUY_PRICE = 90.0
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
RECEIVING_EMAIL = os.getenv("RECEIVING_EMAIL")

response = requests.get(url=URL, headers={"User-Agent": "Defined"})
html_text = response.text

soup = BeautifulSoup(html_text, "html.parser")

product_price = soup.find(name="span", class_="a-offscreen").text
formatted_product_price = product_price.replace('£', '')

product_name = soup.find(name="span", id="productTitle").text
formatted_product_name = product_name.replace("\n", "")

# Replace &nbsp; (non-breaking space character) in the HTML title text with spaces
final_product_name = formatted_product_name.replace(u'\xa0', " ")

email_body = f"{final_product_name} is now on sale for GBP{formatted_product_price}!\n{URL}"

if float(formatted_product_price) < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECEIVING_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{email_body}"
                            )
