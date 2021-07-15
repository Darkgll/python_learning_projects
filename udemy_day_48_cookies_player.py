from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "F:\Programming\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# the game about making a cookies
web_page = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(web_page)

cookie_click = driver.find_element_by_id("cookie")
store = driver.find_element_by_id("store")

game_on = True
time_on = time.time() + 5
timeout = time.time() + 60*5

while game_on:

    cursor_click = driver.find_element_by_id("buyCursor")
    cursor_cost = int(cursor_click.text.split(' ')[2].split('\n')[0].replace(",", ""))

    grandma_click = driver.find_element_by_id("buyGrandma")
    grandma_cost = int(grandma_click.text.split(' ')[2].split('\n')[0].replace(",", ""))

    factory_click = driver.find_element_by_id("buyFactory")
    factory_cost = int(factory_click.text.split(' ')[2].split('\n')[0].replace(",", ""))

    mine_click = driver.find_element_by_id("buyMine")
    mine_cost = int(mine_click.text.split(' ')[2].split('\n')[0].replace(",", ""))

    shipment_click = driver.find_element_by_id("buyShipment")
    shipment_cost = int(shipment_click.text.split(' ')[2].split('\n')[0].replace(",", ""))

    alchemy_click = driver.find_element_by_id("buyAlchemy lab")
    alchemy_cost = int(alchemy_click.text.split(' ')[3].split('\n')[0].replace(",", ""))

    portal_click = driver.find_element_by_id("buyPortal")
    portal_cost = int(portal_click.text.split(' ')[2].split('\n')[0].replace(",", ""))

    time_m_click = driver.find_element_by_id("buyTime machine")
    time_m_cost = int(time_m_click.text.split(' ')[3].split('\n')[0].replace(",", ""))

    money = int(driver.find_element_by_id("money").text.replace(",", ""))

    if time.time() > time_on:
        if time_m_cost <= money:
            time_m_click.click()
        elif portal_cost <= money:
            portal_click.click()
        elif alchemy_cost <= money:
            alchemy_click.click()
        elif shipment_cost <= money:
            shipment_click.click()
        elif mine_cost <= money:
            mine_click.click()
        elif factory_cost <= money:
            factory_click.click()
        elif grandma_cost <= money:
            grandma_click.click()
        elif cursor_cost <= money:
            cursor_click.click()
        else:
            continue
        time_on = time.time() + 10
        time.sleep(0.1)
    cookie_click.click()

    if time_on >= timeout:
        print(driver.find_element_by_id("cps").text)
        game_on = False

driver.quit()
