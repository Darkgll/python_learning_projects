from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


driver_path = PATH TO YOUR DRIVER (like Chromedriver)
brave_path = PATH TO YOUR BROWTHER

account_name = ""
account_password = ""

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_extension("") # You may add an extension if you need
option.add_argument("--start-maximized") # instead of this you also can hide chat by clicking chat hide button

driver = webdriver.Chrome(executable_path=driver_path, options=option)

# Use the link with all job requirements that you want below
linkedin_settings = ""
driver.get(linkedin_settings)
time.sleep(2)


def sleep_sec():
    time.sleep(1)


sleep_sec()
sing_in = driver.find_element_by_css_selector(".join-form__form-body-subtext .form-toggle")
sing_in.click()
sleep_sec()
login_input = driver.find_element_by_id("login-email")
login_input.send_keys(account_name)
sleep_sec()
passwd_input = driver.find_element_by_id("login-password")
passwd_input.send_keys(account_password)
sleep_sec()
passwd_input.send_keys(Keys.ENTER)
sleep_sec()
try:
    not_remember = driver.find_element_by_id("remember-me-prompt__form-secondary")
    not_remember.click()
except NoSuchElementException:
    pass
sleep_sec()

jobs_list = driver.find_elements_by_class_name("jobs-search-results__list-item")
for job in jobs_list:
    job.click()

    sleep_sec()

    save_job = driver.find_element_by_class_name("jobs-save-button")
    save_job.click()
    sleep_sec()
    scroll_down = driver.find_element_by_class_name('jobs-search__right-rail')
    scroll_down.click()
    scroll_down.send_keys(Keys.END)
    html = driver.find_element_by_tag_name("html")
    for _ in range(45):
        time.sleep(0.1)
        html.send_keys(Keys.ARROW_DOWN)
    sleep_sec()
    try:
        follow_company = driver.find_element_by_class_name("follow")
        follow_company.click()
    except NoSuchElementException:
        continue
    sleep_sec()
sleep_sec()


driver.quit()

print("Jobs are saved.")

