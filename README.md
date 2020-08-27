# Web_Scraping_Quotes

This repo contains code (my own implementation) for a __Web Scraping Project__ from the Udemy course "The Modern Python 3 Bootcamp", which is the course that brought Python to my life and enabled me to start utilising it personally and professionally for data analysis, process automation and many other activities!

In the context of this project I built a quotes guessing game. When run, our program will scrape a website for a collection of quotes, pick one at random and display it. The player will have four chances to guess who said the quote. After every wrong guess a hint about the author's identity will be provided.

There are 3 files in the repo. The file __web_scraping_initial.py__ provides a first implementation, whereas the files __csv_scraper.py__ and __csv_quote_game.py__, utilised in conjunction with each other, provide a refactored, optimised solution. More specifically, in the latter case I refactored the quotes game initial script by defining functions and by using the CSV library so that we do not need to scrape every time at the beginning of the process. We instead run the `csv_scraper` file. This will generate a `quotes.csv` file in which the scraped data is saved so that we can recall it whenever we want (we moved this functionality to a separate file because we do not want to be saving to a CSV file every time). We will finally utilise the `csv_quote_game` file to play the game.

<ins>How to run:</ins>

   - Install the `Requests` module [(pypi link)](https://pypi.org/project/requests/).
     
   - Install the `Beautiful Soup` module [(pypi link)](https://pypi.org/project/beautifulsoup4/).

<ins>Specifications</ins>

1) The file, when run, will grab data on every quote from the website http://quotes.toscrape.com
2) For each quote the following data will be pulled: the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio.
3) Next, the user will be asked who said the quote. The player will have four guesses remaining.
4) After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
5) After every incorrect guess, the player receives a hint about the author.
    - For the first hint, another request will be made to the author's bio page (this is why we originally scrape this data), and we will provide         the player with the author's birth date and location.
    - Regarding the second and third hints we will provide the first letter of the author's first name and the first letter of the author's last         name respectively.
6) When the game is over, the player will be asked if they want to play again. If yes, the game will restart with a new quote. If not, the program is complete.
