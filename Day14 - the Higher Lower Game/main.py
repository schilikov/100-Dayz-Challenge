from ART import logo, vs
from game_data import data
import random

print(logo)


def pick_random(game_data):
    list_length = len(game_data)
    list_item = random.randint(0, list_length - 1)
    data_item = game_data[list_item]

    return data_item


def print_the_picks(first_choice, second_choice):
    vowels = ["a", "e", "i", "o", "u", "y"]
    if first_choice['description'][0].lower() in vowels:
        article = "an"
    else:
        article = "a"

    print(f"Compare A: {first_choice['name']}, {article} {first_choice['description']}, from {first_choice['country']}.")

    print(vs)

    print(f"Against B: {second_choice['name']}, {article} {second_choice['description']}, from {second_choice['country']}.")


# def check_the_winner(first_pick, second_pick):


total_points = 0
game_end = False

first_pick = pick_random(data)
second_pick = pick_random(data)

while first_pick == second_pick:
    second_pick = pick_random(data)

print_the_picks(first_pick, second_pick)

pick = input("Who has more followers? Type 'A' or 'B':").lower()

