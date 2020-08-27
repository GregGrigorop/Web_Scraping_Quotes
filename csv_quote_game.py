import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com" # capitalised because it's a constant (convention)

def read_quotes(filename):
	with open(filename, "r", encoding="utf-8") as file: # added encoding="utf-8" as otherwise I get --> UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 141: character maps to <undefined>
		csv_reader = DictReader(file)
		return list(csv_reader) # if we don't use list here we'll get a list with OrderedDict elements, instead of just a list
		# we can use this for loop to see the list with the OrderedDict elements we would get if we didn't use list(csv_reader)
		# for thing in csv_reader:
		# 	print(thing)

def start_game(quotes):
	quote = choice(quotes)
	remaining_guesses = 4
	print("Here's a quote")
	print(quote["text"])
	guess = ''
	while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
		guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}.\n")
		if guess.lower() == quote["author"].lower():
			print("YOU GOT IT RIGHT!")
			break
		remaining_guesses -= 1
		print_hint(quote, remaining_guesses)
		
	again = ''
	while again.lower() not in ('y', 'yes', 'n', 'no'): # making sure the user will give 1 of these 4 answers
		again = input("Would you like to play again? (y/n)? ")
	if again.lower() in ('yes', 'y'):
		return start_game(quotes)
	else:
		print("OK, GOODBYE!")

def print_hint(quote, remaining_guesses):
	if remaining_guesses == 3:
			res = requests.get(f"{BASE_URL}{quote['bio-link']}")
			soup = BeautifulSoup(res.text, "html.parser")
			birth_date = soup.find(class_="author-born-date").get_text()
			birth_place = soup.find(class_="author-born-location").get_text()
			print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
	elif remaining_guesses == 2:
		print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
	elif remaining_guesses == 1:
		last_initial = quote["author"].split()[-1][0]
		print(f"Here's a hint: The author's last name starts with: {last_initial}")
	else:
		print(f"Sorry, you've run out of guesses. The answer was {quote['author']}")

quotes = read_quotes("quotes.csv")
# here we don't scrape any quotes, we use the data saved in the "quotes.csv" file instead (we only scrape for the 1st hint)
start_game(quotes)