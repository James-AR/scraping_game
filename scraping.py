import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

quotes_list = []
base_url = "http://quotes.toscrape.com/"
url = "/page/1"

while url:
    response = requests.get(f"{base_url}{url}")
    print(f"scraping {base_url}{url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all(class_="quote")
    
    for quote in quotes:
        quotes_list.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "author_bio": quote.find("a")["href"]
        })
    next_btn = soup.find(class_="next")
    url = next_btn.find("a")["href"] if next_btn else None
    sleep(2)
print(quotes_list)