from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

response = requests.get(url= "https://www.zillow.com/homes/Daphne,-AL_rb/", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".list-card-details li")
all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]


for element in all_price_elements:
    try:
        price = element.select(".list-card-price")[0].contents[0]
        print(price)
    except IndexError:
        print('Multiple listings for the card')
        # price = element.select(".list-card-details li")[0].contents[0]
        price = "NA"
    finally:
        all_prices.append(price)

chrome_driver_path = "/Users/dra7400/Documents/Development/chromedriver"
service = Service("/Users/dra7400/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=service)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf0QJnodMvoX_3lds4KFCSxG8j8W2oCKUFPs_49gN0aVQ4dyQ/viewform?usp=sf_link")
    time.sleep(2)
    address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input' )
    price = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
