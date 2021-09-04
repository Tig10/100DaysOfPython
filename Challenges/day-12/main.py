from art import logo
import random

print(logo)
print('Welcome to Guess The Number Game!')
print('I\'m thinking of a number between 1 and 100.')


def compare(user_guess, rand_numb):
    if user_guess == rand_numb:
        return '\tYou got it. Yay!'
    elif user_guess > rand_numb:
        return '\tToo high. Try a lower number.'
    elif user_guess < rand_numb:
        return '\tToo low. Try a higher number.'


def game():
    number = random.randint(1, 100)
    level = input('Guess the number. Type \'easy\' ore \'hard\' level: ')
    if level == 'easy':
        available_guesses = 10
    elif level == 'hard':
        available_guesses = 5

    while available_guesses != 0:
        print(f'\tYou have {available_guesses} guesses remaining.')
        guess = int(input('Make a guess: '))
        print(compare(guess, number))
        if guess == number:
            break
        available_guesses -= 1

    if guess != number:
        print(f'Game over! The number is {number}.')
    elif guess == number:
        print(f'Congratulations! {guess} is correct!')


game()

