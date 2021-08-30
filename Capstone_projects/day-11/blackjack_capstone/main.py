# main.py
# 100 Days of Python - Blackjack capstone project

import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
player_cards = []
game_over = False
replay = False


def deal_card(card_list):
    rand = random.choice(card_list)
    return rand


def hit(num, member_cards):
    for _ in range(num):
        card = deal_card(cards)
        member_cards.append(card)
    return member_cards


def deal_player(num):
    for _ in range(num):
        card = deal_card(cards)
        player_cards.append(card)
    return player_cards


def calculate_score(dealt_cards):
    if len(dealt_cards) == 2:
        if 11 in dealt_cards and 10 in dealt_cards:
            return 0
    if 11 in dealt_cards:
        if sum(dealt_cards) > 21:
            dealt_cards.remove(11)
            dealt_cards.append(1)
    return sum(dealt_cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw!'
    elif computer_score == 21:
        return 'You lose, dealer has a Blackjack! 😎'
    elif user_score == 21:
        return 'You win, you have a Blackjack! 😎'
    elif user_score > 21:
        return 'You lose! with a bust! 😫'
    elif computer_score > 21:
        return 'You win! dealer busted! 😃'
    elif user_score > computer_score:
        return 'You win! 😃'
    elif computer_score > user_score:
        return 'You lose! 😫'


def reset():
    player_cards.clear()
    dealer_cards.clear()


player_set = hit(2, player_cards)
dealer_set = hit(2, dealer_cards)

while not game_over:
    if len(dealer_cards) == 0 and len(player_cards) == 0:
        player_set = hit(2, player_cards)
        dealer_set = hit(2, dealer_cards)

    player_score = calculate_score(player_set)
    dealer_score = calculate_score(dealer_set)
    if player_score == 0:
        player_score = 21
    if dealer_score == 0:
        dealer_score = 21

    print(f'\tYour cards: {player_set}, current score: {player_score}')
    print(f'\tComputer\'s first card: {dealer_set[0]}')
    play_on = input('Type \'y\' to get another card, type \'n\' to pass: ')

    if play_on == 'n':
        while dealer_score < 17 and dealer_score != 0:
            dealer_set = hit(1, dealer_cards)
            dealer_score = calculate_score(dealer_set)
        print(f'\tYour final hand: {player_set}, final_score: {player_score}')
        print(f'\tComputer\'s final hand: {dealer_set}, final score: {dealer_score}')
        result = compare(player_score, dealer_score)
        print(result)
        replay = input('Do you want to replay? \'y\' or \'n\': ')
        if replay == 'n':
            game_over = True
        else:
            replay = True
            reset()
    else:
        player_set = hit(1, player_cards)
        player_score = calculate_score(player_set)
        if player_score > 21:
            print(f'\tYour final hand: {player_set}, final score: {player_score}')
            print(f'\tComputer\'s final hand: {dealer_set}, final score: {dealer_score}')
            result = compare(player_score, dealer_score)
            print(result)
            replay = input('Do you want to replay? \'y\' or \'n\': ')
            if replay == 'n':
                game_over = True
            else:
                replay = True
                reset()
        if dealer_score > 21:
            print(f'\tYour final hand: {player_set}, final score: {player_score}')
            print(f'\tComputer\'s final hand: {dealer_set}, final score: {dealer_score}')
            result = compare(player_score, dealer_score)
            print(result)
            replay = input('Do you want to replay? \'y\' or \'n\': ')
            if replay == 'n':
                game_over = True
            else:
                replay = True
                reset()

