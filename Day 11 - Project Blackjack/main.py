################# PROJECT - BlackJack Game ####################

################# Our Blackjack House Rules ###################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

###############################################################
import random
from replit import clear
from ART import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    if len(list_of_cards) == 2 and sum(list_of_cards) == 21:
        return 0

    elif sum(list_of_cards) > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Opponent has Blackjack. You Lose."
    elif user_score == 0:
        return "You Win with Blackjack."
    elif user_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Opponent went over 21. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    game_end = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True

        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}. Final score: {user_score}")
    print(f"Computer`s final hand: {computer_cards}. Final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
