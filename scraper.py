import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com/"

def scrape_quotes():
    quotes_list = []
    url = "/page/1"
    while url:
        response = requests.get(f"{BASE_URL}{url}")
        response.encoding = 'utf-8'
        print(f"scraping {BASE_URL}{url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all(class_="quote")
        
        for quote in quotes:
            quotes_list.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(2)
    return quotes_list

def write_quotes(quotes):
    with open("quotes.csv", "w", encoding='utf-8', newline= '') as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)