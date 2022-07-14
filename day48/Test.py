from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import threading

service = Service("/Users/dra7400/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.ID, "bigCookie")


def buy_stuff():
    threading.Timer(30, buy_stuff).start()
    upgrades_prices = driver.find_elements(By.CSS_SELECTOR, ".upgrade.enabled")
    if upgrades_prices:
        upgrades_prices[-1].click()

    products_prices = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")
    if products_prices:
        products_prices[-1].click()


buy_stuff()
while True:
    cookie.click()