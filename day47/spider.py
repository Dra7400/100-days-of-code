import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

url = "https://www.amazon.com/gp/product/B07WVHYWGG/ref=ask_ql_qh_dp_hza"
Buy_Price = 500

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
print(title)
price = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
price_decimal = soup.find(name="span", class_="a-price-fraction").getText().split(".")[0]
price_as_float = float(price + "." + price_decimal)
print(price_as_float)
if price_as_float < Buy_Price:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login('david.r.adams@gmail.com', 'Cricket040419!')
        connection.sendmail(
            from_addr='david.r.adams@gmail.com',
            to_addrs='dra7400@gmail.com',
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
        
