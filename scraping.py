import requests
from bs4 import BeautifulSoup
import csv

response = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')