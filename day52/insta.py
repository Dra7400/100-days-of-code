import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "/Users/dra7400/Documents/Development/chromedriver"
service = Service("/Users/dra7400/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=service)
SIMILAR_ACCOUNT = "madamebrocante"
USERNAME = "dra7400@gmail.com"
PASSWORD = "Cricket0404!"


class InstaFollower:

    def __init__(self, path):
        self.driver = driver

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='followers')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
        random_no = random.randint(2, 50)
        for i in range(random_no):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)



    def follow(self):
        all_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value='li button')
        for button in all_buttons:
            if button.text == 'Follow':
                time.sleep(1)
                button.click()
                rand_time = random.randint(2, 40)
                print(rand_time)
                time.sleep(rand_time)
            # else:
            #     driver.execute_script("window.scrollTo(0, 200);")


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
