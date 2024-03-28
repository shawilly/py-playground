import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

response = requests.get(
    'https://www.wordunscrambler.net/word-list/wordle-word-list')

soup = BeautifulSoup(response.text, 'html.parser')

words_html = soup.find_all('li', class_="invert light")

words = []

for word_html in words_html:
    word_soup = BeautifulSoup(str(word_html), 'html.parser')
    a = str(word_soup.find('a'))
    word = re.search(r'<a.*?>(.*?)</a>', a).group(1)
    words.append(word)
