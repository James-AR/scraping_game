import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com/"

def read_quotes(filename):
    with open(filename, "r", encoding='utf-8') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    guess = ""
    print(quote["text"])

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? You have {remaining_guesses} guesses remaining.\n")
        if guess.lower() == quote['author'].lower():
            print('You got it!')
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, 'html.parser')
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: Author was born {birth_place} on {birth_date}")
        elif remaining_guesses == 2:
            print(f"Here's a hint: Author's first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"Here's a hint: Author's last name starts with {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    again= ''
    while again.lower() not in ['yes', 'y', 'no', 'n']:
        again = input(f"Would you like to play again? y/n\n")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print('Okay!')

quotes = read_quotes("quotes.csv")
start_game(quotes)