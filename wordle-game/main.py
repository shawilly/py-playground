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


introduction()

play_again = "y"

while play_again == "y":
    word = random.choice(words).lower()
    print(word)
    keyboard_letters = dict.fromkeys(string.ascii_lowercase, "grey")

    for attempt in range(1, 7):
        guess = input().lower()

        if guess not in words or len(guess) != 5 or not guess.isalpha():
            print(colored("Invalid word. Please try again", "red"))
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
                    this_word = this_word.replace(guess[i], "_")
                else:
                    result[i] = colored(guess[i], "grey")

            for i in range(len(this_word)):
                if guess[i] in this_word:
                    result[i] = colored(guess[i], "yellow")
                    this_word = this_word.replace(guess[i], "_")

            print(''.join(result), end="\n\n")

        if guess == word:
            print(
                colored("\nYou win! You got the word in {attempt} tries", "green"))
            break
        elif attempt == 6:
            print(colored("\nYou lose! The word was {word}", "red"))

    play_again = input("Do you want to play again? (y/n): ")
