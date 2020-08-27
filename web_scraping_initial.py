import requests
from bs4 import BeautifulSoup
from random import randint

response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
quotes_general = soup.find_all("div",class_="quote")
# print(len(quotes_general))
# print(quotes_general)

# quotes = soup.find_all("span",class_="text")
# print(quotes)
# print(len(quotes))
def populate_dict(key,d,value):
	if key in d:
		result = d[key].append(value)
	else:
		result = d[key] = [value]
	return result

info = {}
# while soup.find(class_="next") != None:
while True:
	for i in quotes_general:
		quote = i.find("span",class_="text").get_text()
		author = i.find("small",class_="author").get_text()
		bio = i.find("a")["href"] # the link can be found inside the 1st anchor tag, so we use this syntax to get this single attribute
		populate_dict("Quote",info,quote)
		populate_dict("Author",info,author)
		populate_dict("Bio",info,bio)
		# OR we don't define the function populate_dict and use the lines below (in the loop)
		# if "Quote" in info:
		# 	info["Quote"].append(quote)
		# else:
		# 	info["Quote"] = [quote]
		# if "Author" in info:
		# 	info["Author"].append(author)
		# else:
		# 	info["Author"] = [author]
		# if "Bio" in info:
		# 	info["Bio"].append(bio)
		# else:
		# 	info["Bio"] = [bio]
	if soup.find(class_="next") == None:
		break
	url = soup.find(class_="next").find("a")["href"]
	response = requests.get("http://quotes.toscrape.com"+url)
	soup = BeautifulSoup(response.text, "html.parser")
	quotes_general = soup.find_all("div",class_="quote")

# OR (for initialising a dictionary with keys and no values)
# from collections import defaultdict
# info = defaultdict(list)
# for i in quotes_general:
# 	quote = i.find("span",class_="text").get_text()
# 	author = i.find("small",class_="author").get_text()
# 	info["Quote"].append(quote)
# 	info["Author"].append(author)

# print(info)
# print(len(info.get("Quote")),len(info.get("Author")),len(info.get("Bio")))
# print(info.get("Quote")[0],info.get("Author")[0],info.get("Bio")[0])
# print(info.get("Quote")[-1],info.get("Author")[-1],info.get("Bio")[-1])

while True:
	# removing from the list any random quote chosen for the user in case he wants to keep playing
	random_quote_index = randint(0,len(info.get("Quote")))
	keys_list = ["Quote","Author","Bio"]
	# I could have used a dictionary here (with "Quote", "Author", "Bio" as keys)
	random_quote_list = []
	for i in keys_list:
		random_quote_list.append(info.get(i).pop(random_quote_index))
	# print(random_quote_list)
	print(len(info.get("Quote"))) # we'll see the len() reduced by 1 here
	reply = input("Here's a quote:\n"+random_quote_list[0]+"\n"+"Who said this? Guesses remaining: 4. ")
	if reply == random_quote_list[1]:
		print("Bullseye!")
	else:
		hint = requests.get("http://quotes.toscrape.com"+random_quote_list[2])
		hint_soup = BeautifulSoup(hint.text, "html.parser")
		dob = hint_soup.find("span",class_="author-born-date").get_text()
		pob = hint_soup.find("span",class_="author-born-location").get_text()
		reply = input("Here's a hint: The author was born on "+dob+" "+pob+"."+"\nWho said this? Guesses remaining: 3. ") # it's better to use a f-string for input()
		if reply == random_quote_list[1]:
			print("Bullseye!")
		else:
			reply = input("Here's a hint: The author's first name starts with "+ \
				"'"+random_quote_list[1][0]+"'"+"\nWho said this? Guesses remaining: 2. ") # a f-string would be better here
			if reply == random_quote_list[1]:
				print("Bullseye!")
			else:
				reply = input("Here's a hint: The author's last name starts with "+ \
					"'"+random_quote_list[1].split()[-1][0]+"'"+ \
					"\nWho said this? Guesses remaining: 1. ") # a f-string would be better here
				if reply == random_quote_list[1]:
					print("Bullseye!")
				else:
					print("Sorry, you've run out of guesses. The answer was "+ \
						random_quote_list[1]+".") # a f-string would be better here
	
	play_again = input("Would you like to play again? (y/n)? ")
	if play_again == "n":
		print("Ok! See you next time!")
		break