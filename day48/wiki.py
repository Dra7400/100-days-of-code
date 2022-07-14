from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/dra7400/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(by=By.NAME, value="fName")
fname.send_keys("David")

lname = driver.find_element(by=By.NAME, value="lName")
lname.send_keys("Adams")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("dra7400@gmail.com")

button = driver.find_element(by=By.CSS_SELECTOR, value="form button")
button.click()


# print(artcle_count.text)
artcle_count.click()