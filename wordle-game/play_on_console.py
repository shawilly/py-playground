import random
import string
import sys
from typing import Literal

from termcolor import colored
from words import fetch_wordle_words


def you_win(attempt, word) -> None:
    yw = colored("\nYou win!", "green", attrs=["bold"])
    p1 = colored("You got the word, ", "green")
    p2 = colored(word, "green", attrs=["bold"])
    p3 = colored(f", in {attempt} tries", "green")
    print(yw + p1 + p2 + p3)


def introduction() -> None:
    print(colored("\n\nWelcome to Wordle!", "green", attrs=["bold"]), end="\n\n")
    print(
        colored(
            "The objective of the game is to guess a 5-letter word in 6 tries.",
            "green",
            attrs=["bold"],
        ),
        end="\n\n\n",
    )


# 6 for good input, 5 for invalid word, 2 for play again
def clear_input(rows) -> None:
    for _ in range(rows):
        sys.stdout.write("\x1b[1A\x1b[2K")
    sys.stdout.write("\x1b[2K")


def print_qwerty_keyboard(key_colors) -> None:
    keyboard: list[list[str]] = [
        ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
        ["z", "x", "c", "v", "b", "n", "m"],
    ]

    for i, row in enumerate(keyboard):
        print(i * " ", end="")
        for key in row:
            colored_key = colored(key, key_colors[key])
            print(colored_key, end=" ")
        print()


introduction()

play_again: Literal["y", "n"] = "y"
invalid_word = False
words = fetch_wordle_words()

while play_again == "y":
    word = random.choice(words).lower()
    keyboard_letters = dict.fromkeys(string.ascii_lowercase, "white")
    attempt = 0

    while attempt < 6:
        print(f"Attempt {attempt} of 6")
        print_qwerty_keyboard(keyboard_letters)

        if invalid_word:
            clear_input(4)
            print(colored("Invalid word. Please enter a 5-letter word.", "red"))
            invalid_word = False
            continue

        guess = input().lower()
        clear_input(6)

        if guess not in words or len(guess) != 5 or not guess.isalpha():
            invalid_word = True
            continue

        attempt += 1

        result = list(guess)

        this_word = word

        for i in range(len(this_word)):
            print(this_word)
            if guess[i] == this_word[i]:
                result[i] = colored(guess[i], "green")
                keyboard_letters[guess[i]] = "green"
                this_word = this_word.replace(guess[i], "_", 1)
            else:
                result[i] = colored(guess[i], "grey")
                if keyboard_letters[guess[i]] != "green":
                    keyboard_letters[guess[i]] = "grey"

        if this_word == "_____":
            you_win(attempt, word)
            break

        for i in range(len(this_word)):
            if guess[i] in this_word:
                result[i] = colored(guess[i], "yellow")
                keyboard_letters[guess[i]] = "green"
                this_word = this_word.replace(guess[i], "_", 1)

        print("".join(result), end="\n\n")

        if attempt == 6:
            print(colored(f"\nYou lose! The word was {word}", "red"))

    play_again = input(colored("\nDo you want to play again? (y/n): ", "blue")).lower()
