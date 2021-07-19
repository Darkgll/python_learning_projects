import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import time

driver_path = "Path to your web driver (like Chromedriver)"
brave_path = "Path to your browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--start-maximized")


link_list = []
price_list = []
move_in_price_list = []
address_list = []
station_list = []

# You can create your own google form
form_url = \
    'https://docs.google.com/forms/d/e/1FAIpQLSeU79ZXAQZl69gtsEDopgFZ2r8yKet8eqzfd0ds5-_5AHlZwA/viewform?usp=sf_link'

# to find an apartment I used https://realestate.co.jp/en
realestatejapan_url = 'https://realestate.co.jp/en/rent/listing?prefecture=JP-13&city=&district=&min_price=&' \
                      'max_price=100000&min_meter=&rooms=&distance_station=&agent_id=&building_type=&building_age=&' \
                      'updated_within=&transaction_type=&internet=1&order=&search=Search'
realestatejapan = requests.get(realestatejapan_url, headers={"User-Agent": "Defined"})


# Beautiful soup to find info
soap = BeautifulSoup(realestatejapan.text, 'html.parser')

rents_links = soap.find_all(name='a', class_='btn btn-primary btn-block hidden-xs below-map')

for link in rents_links:

    link_address = link.get('href')
    if not link_address.startswith('https://realestate.co.jp'):
        link_address = 'https://realestate.co.jp' + link.get('href')
    link_list.append(link_address)
    print(link_address)

    link_info = requests.get(link_address)
    rent_soap = BeautifulSoup(link_info.text, 'html.parser')

    price = rent_soap.find(name="strong", class_="price").string
    price_list.append(price)
    print(price)

    move_in_price = rent_soap.find_all(name="dd", class_='text-heavy text-right mt-10')[1].string
    move_in_price_list.append(move_in_price)
    print(move_in_price)

    address = rent_soap.find(name="dd", itemprop="address").string
    address_list.append(address)
    print(address)

    station = rent_soap.find(name="dd", class_='text-left').text.strip()
    station = station.replace("\n", ": ")
    station = station.replace("\t", "")
    station_list.append(station)
    print(station)


print(link_list)
print(len(link_list))
print(price_list)
print(len(price_list))
print(move_in_price_list)
print(len(move_in_price_list))
print(address_list)
print(len(address_list))
print(station_list)
print(len(station_list))

# now we can input all our info into the google form
driver = webdriver.Chrome(executable_path=driver_path, options=option)

for number in range(len(link_list)):
    driver.get(form_url)
    time.sleep(1)

    link_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link_list[number])
    time.sleep(1)

    price_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[number])
    time.sleep(1)

    move_in_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    move_in_input.send_keys(move_in_price_list[number])
    time.sleep(1)

    address_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[number])
    time.sleep(1)

    station_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    station_input.send_keys(station_list[number])
    time.sleep(1)

    # send all info
    send_info = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    send_info.click()
    time.sleep(5)


driver.quit()
