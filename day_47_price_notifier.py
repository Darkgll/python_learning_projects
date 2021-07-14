import requests
from bs4 import BeautifulSoup
import smtplib
import lxml  # you may need it instead of 'html.parser'
from pprint import pprint

# to check prices history use https://camelcamelcamel.com
needed_price = 85

# I use a second gmail account to send a notification message
g_my_email = None
g_password = None

item_url = "https://www.amazon.com/Instant-Pot-60-Max-Electric/dp/B077T9YGRM/ref=ex_alt_wg_d"

# You may need to add headers as "Accept-Language" and "User-Agent". You can find them at http://myhttpheader.com/
response = requests.get(item_url, headers={"User-Agent": "Defined"})
response_text = response.text
print(response_text)

soap = BeautifulSoup(response_text, 'html.parser')
pprint(soap)

item_name = soap.find(id="productTitle")
item_price_tag = soap.find(id="priceblock_ourprice")
# print(item_price_tag)

try:
    item_price = float(item_price_tag.getText()[1:])
    # print(item_price)
    if item_price < needed_price:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=g_my_email, password=g_password)
            connection.sendmail(from_addr=g_my_email, to_addrs="sanamyi7@gmail.com",
                                msg=f'Subject:There is a good price!'
                                    f'\n\n{item_name} is now ${item_price}! Check it here:\n{item_url}')
except AttributeError as exc:
    pass
    # print(exc)
