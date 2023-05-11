# import rest of modules used in project
# import logo for art.py
from art import logo

import os
import random


def clear():
    """Clears the console across operating systems"""
    command = 'clear'
    if os.name == ('nt', 'dos'):
        command = 'cls'

    os.system(command)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(cards):
    """Take a list of cards and return score calculated"""
    if sum(cards) == 21 and len(cards) == 2:
        # return 0 to rep blackjack hand
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Pass in both the user and computer score as arguments"""
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    elif user_score == 0:
        return "Win with blackjack! WOOOO!"
    elif user_score > 21:
        return "You went over. You lose 😃"
    elif computer_score > 21:
        return "You win. Opponent Busted 🤪"
    elif user_score > computer_score:
        return "you Win 😎"
    else:
        return "You Lose! BOOOO! 🥺"


def play_game():
    """THis func will be run so the game begins"""
    print(logo)

    user_cards = []
    computer_cards = []

    is_game_over = False

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}, current score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card (hit), type 'n' to stand: ").lower()

            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # while loop to keep computer playing
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    # f string print out final scores
    print(f"Your final hand {user_cards}, your final score {user_score}")
    print(f"Computer's final hand {computer_cards}, computer's final score {computer_score}")

    print(compare(user_score, computer_score))


while input("Want to play Blackjack? Type 'y' to start, hit enter to leave: ").lower() == 'y':
    clear()
    play_game()
