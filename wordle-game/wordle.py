import random
from words import fetch_wordle_words

def get_word() -> str:
    return random.choice(fetch_wordle_words()).lower()
