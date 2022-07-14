from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_URL = "https://twitter.com/home"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_EMAIL = "dra7400@gmail.com"
TWITTER_PASSWORD = "Lone7400!"
CHROME_DRIVER_PATH = Service("/Users/dra7400/Documents/Development/chromedriver")

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self, speed_url):
        self.driver.get(speed_url)
        print("Let's open Speed Test WebSite")
        sleep(15)
        go_button = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        go_button.click()
        print("Let's check internet speed. That's will take 60 second")
        sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"internet speed {self.down}")
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f"{self.up} upload")

    def tweet_at_provider(self, twitter_url):
        self.driver.get(twitter_url)
        print("Opening Twitter.com")
        sleep(10)
        enter_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        enter_email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        next_button.click()
        print("You entered your e-mail")
        sleep(10)
        enter_password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        enter_password.send_keys(TWITTER_PASSWORD)
        print("You entered your password")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]')
        login_button.click()
        print("You logged in!")
        sleep(5)
    # Click on tweet
        click_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        click_tweet.click()
        sleep(3)
        print("Now I will send tweet...")
    # Enter your tweet message
        enter_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        enter_tweet.send_keys(f'hello dear idk who! my internet speed is {self.down} download/ {self.up} upload' f' {PROMISED_DOWN} down/ {PROMISED_UP} up?')
        sleep(3)
        print("Tweet is ready to post")
    # Post your tweet
        post_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        post_tweet.click()
        print("Tweet is sent!!! Good job!!!")
        sleep(10)
        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed(SPEED_TEST_URL)
# bot.tweet_at_provider(TWITTER_URL)
