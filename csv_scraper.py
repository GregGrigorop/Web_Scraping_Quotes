import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com" # capitalised because it's a constant (convention)

def scrape_quotes():
	all_quotes = []
	url = "/page/1"
	while url:
		res = requests.get(f"{BASE_URL}{url}")
		print(f"Now scraping {BASE_URL}{url}...")
		soup = BeautifulSoup(res.text, "html.parser") # if we don't specify a type of markup to use we'll get a warning
		quotes = soup.find_all(class_="quote")

		for quote in quotes:
			all_quotes.append({
				"text":quote.find(class_="text").get_text(),
				"author":quote.find(class_="author").get_text(),
				"bio-link":quote.find("a")["href"]
				})
		next_button = soup.find(class_="next")
		url = next_button.find("a")["href"] if next_button else None # in the last page there is no "next" button, so url will be set to None and the loop will stop
		sleep(1) # with this our code will be halted for 1 sec (so that we don't overload the server of the website we are scraping)
		# here we need sleep as we would scrape the website once per week/month for example to check for new quotes (not everytime we play the game)
	return all_quotes

# write quotes to a csv file using a function
def write_quotes(quotes):
	with open("quotes.csv", "w", encoding="utf-8") as file: # added encoding="utf-8" as otherwise I get --> UnicodeEncodeError: 'charmap' codec can't encode character '\u2032' in position 1: character maps to <undefined>
		headers = ['text', 'author', 'bio-link']
		csv_writer = DictWriter(file, fieldnames = headers)
		csv_writer.writeheader()
		for quote in quotes:
			csv_writer.writerow(quote) # quote is already a dictionary each time so this works fine

quotes = scrape_quotes()
write_quotes(quotes)