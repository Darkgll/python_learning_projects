from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time


driver_path = PATH TO YOUR DRIVER (like Chromedriver)
brave_path = PATH TO YOUR BROWTHER

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=driver_path, options=option)

tinder = "https://tinder.com/app/recs"
driver.get(tinder)
time.sleep(2)

opportunity = 50  # how many pages you want to swap
email = ""  # Your email to login
password = ""  # Your password to login

base_window = driver.window_handles[0]


def sleep_sec():
    time.sleep(1)


sleep_sec()
sing_in = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
sing_in.click()
sleep_sec()
choose_facebook = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div[1]/div/div[3]/span/button')
choose_facebook.click()
sleep_sec()
log_in_facebook = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div[1]/div/div[3]/span/div[2]/button')
log_in_facebook.click()
sleep_sec()
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
login_input = driver.find_element_by_id("email")
login_input.send_keys(email)
sleep_sec()
passwd_input = driver.find_element_by_id("pass")
passwd_input.send_keys(password)
sleep_sec()
passwd_input.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)


# now it's time to swap in tinder
time.sleep(12)
try:
    allow_location = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[1]')
    allow_location.click()
except NoSuchElementException:
    pass
try:
    not_allow_not = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[2]')
    not_allow_not.click()
except NoSuchElementException:
    pass
try:
    cookies = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[2]/div/div/div[1]/button')
    cookies.click()
except NoSuchElementException:
    pass

time.sleep(30)


# you may use at least two methods to make a swap
# for the purpose of testing new app i decided to reject every person
for _ in range(opportunity):
    time.sleep(3)
    swap = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
    try:
        swap.click()
    except ElementNotInteractableException:
        time.sleep(3)
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.LEFT)


driver.quit()
