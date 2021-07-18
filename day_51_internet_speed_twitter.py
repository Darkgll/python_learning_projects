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

TWITTER_EMAIL = ""  # Your email to login
TWITTER_PASSWORD = ""  # Your password to login


class InternetSpeedTwitterBot:
    def __init__(self):
        self.speed_test = driver.get("https://www.speedtest.net/")
        self.down = None
        self.up = None
        time.sleep(10)

    def get_internet_speed(self):
        go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(55)  # make sure it will be enough to make a full speed test
        self.down = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
            '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
            '/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        time.sleep(1)

    def tweet_info(self):
        twitter = "https://twitter.com/login"
        driver.get(twitter)
        time.sleep(2)
        email = driver.find_element_by_name('session[username_or_email]')
        email.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        pswrd = driver.find_element_by_name('session[password]')
        pswrd.send_keys(TWITTER_PASSWORD)
        pswrd.send_keys(Keys.ENTER)
        time.sleep(2)
        make_tweet = driver.find_element_by_css_selector(
            'div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        make_tweet.send_keys(f'Python auto-tweet test.'  # You may change your twit as you want
                             f'\nInternet speed today:'
                             f'\nDownload: {self.down}'
                             f'\nUpload: {self.up}')
        send_tweet = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]'
            '/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send_tweet.click()


internet_speed_tweet = InternetSpeedTwitterBot()
internet_speed_tweet.get_internet_speed()
internet_speed_tweet.tweet_info()

time.sleep(2)

driver.quit()

