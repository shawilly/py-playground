import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os

def fetch_wordle_words() -> list[str]:
    # Check if the word list is already downloaded
    if os.path.exists('wordle_words.txt'):
        with open('wordle_words.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]

    response = requests.get(
        'https://www.wordunscrambler.net/word-list/wordle-word-list')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        words_html = soup.find_all('li', class_="invert light")

        words = []
        for word_html in words_html:
            word_text = word_html.find('a').text.strip()
            words.append(word_text)

        # Save the words to a local file
        with open('wordle_words.txt', 'w') as file:
            file.write('\n'.join(words))

        return words
    else:
        print("Failed to fetch the word list.")
        return []