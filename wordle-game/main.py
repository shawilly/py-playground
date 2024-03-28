import random
import sys
from termcolor import colored
import string
from words import words


def introduction():
    print(colored("\n\nWelcome to Wordle!",
          "green", attrs=["bold"]), end="\n\n")
    print(colored("The objective of the game is to guess a 5-letter word in 6 tries.",
          "green", attrs=["bold"]), end="\n\n")


def clear_input():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


def print_qwerty_keyboard(key_colors):
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]

    for i, row in enumerate(keyboard):
        print(i * " ", end="")
        for key in row:
            colored_key = colored(key, key_colors[key])
            print(colored_key, end=" ")
        print()


introduction()

play_again = "y"

while play_again == "y":
    word = random.choice(words).lower()
    keyboard_letters = dict.fromkeys(string.ascii_lowercase, "white")

    for attempt in range(1, 7):
        print_qwerty_keyboard(keyboard_letters)
        guess = input().lower()

        if guess not in words or len(guess) != 5 or not guess.isalpha():
            print(colored("Invalid word.", "red"))
            if attempt - 1 > 0:
                attempt -= 1
            continue

        clear_input()

        result = list(guess)

        if guess != word:
            this_word = word

            for i in range(len(this_word)):
                if guess[i] == this_word[i]:
                    result[i] = colored(guess[i], "green")
                    keyboard_letters[guess[i]] = "green"
                    this_word = this_word.replace(guess[i], "_")
                else:
                    result[i] = colored(guess[i], "grey")
                    keyboard_letters[guess[i]] = "grey"

            for i in range(len(this_word)):
                if guess[i] in this_word:
                    result[i] = colored(guess[i], "yellow")
                    keyboard_letters[guess[i]] = "green"
                    this_word = this_word.replace(guess[i], "_")

            print(''.join(result), end="\n\n")

        if guess == word:
            print(
                colored(f"\nYou win! You got the word, {word}, in {attempt} tries", "green", attrs=["bold"]))
            break
        elif attempt == 6:
            print(colored(f"\nYou lose! The word was {word}", "red"))

    play_again = input(colored("\nDo you want to play again? (y/n): ", "blue")).lower()
