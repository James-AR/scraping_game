import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')

quotes_list = []
quotes = soup.find_all(class_="quote")
for quote in quotes:
    quotes_list.append({
        "text": quote.find(class_="text").get_text()
        "author": quote.find(class_="author").get_text()
    })