from replit import clear

from ART import logo, vs
from game_data import data
import random


def pick_random():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account['name']
    description = account['description']
    country = account['country']

    vowels = ["a", "e", "i", "o", "u", "y"]
    if account['description'][0].lower() in vowels:
        article = "an"
    else:
        article = "a"

    return f"{name}, {article} {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
      and returns True if they got it right.
      Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_end = False
    second_pick = pick_random()

    while not game_end:
        first_pick = second_pick
        second_pick = pick_random()

        while first_pick == second_pick:
            second_pick = pick_random()

        print(f"Compare A: {format_data(first_pick)}.")
        print(vs)
        print(f"Against B: {format_data(second_pick)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = first_pick["follower_count"]
        b_follower_count = second_pick["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_end = True
            print(f"Sorry, that's wrong. Final score: {score}")


game()
