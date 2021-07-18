from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

driver_path = "PATH TO YOUR DRIVER (like Chromedriver)"
brave_path = "PATH TO YOUR BROWTHER"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--start-maximized")

INSTAGRAM_EMAIL = ""  # Your email
INSTAGRAM_PASSWORD = ""  # Your password


# this app will follow accounts which is following target account (not "followers", but "following")
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path, options=option)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(4)
        email = self.driver.find_element_by_name('username')
        email.send_keys(INSTAGRAM_EMAIL)
        password = self.driver.find_element_by_name('password')
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/yamaha_bike/')  # You may choose whatever account you like
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(4)

    def follow(self):
        time.sleep(1)
        times_to_key_down = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
        print(times_to_key_down.text)
        times = int(times_to_key_down.text) // 12  # This will help you to see all the following accounts
        for _ in range(times):
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/ul/div/li[1]').click()
            self.driver.find_element_by_tag_name('html').send_keys(Keys.END)
            time.sleep(1)
        following = self.driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[3]/ul/div/li')
        for account in following:
            time.sleep(1)
            print(account.text)
            try:
                follow = account.find_element_by_tag_name('button')
                follow.click()
            except ElementClickInterceptedException:
                time.sleep(1)
                cancel_unfollow = self.driver.find_element_by_xpath(
                    '/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_unfollow.click()
        time.sleep(1)
        self.driver.quit()


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
