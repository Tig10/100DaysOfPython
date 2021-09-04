from art import logo, vs
from game_data import data
import random
import os

print(logo)

def rand_num():
    end_num = len(data)
    rand_num = random.randint(0, end_num-1)
    return rand_num

def compare(f_count1, f_count2):
    data_list = [f_count1, f_count2]
    result = sorted(data_list)
    return result

game_over = False
score = 0
while not game_over:
    if score > 0:
        entry_a = entry_b
        print(f"Compare A: {entry_a['name']}, {entry_a['description']}, from {entry_a['country']}.")
    else:
        entry_a = data[rand_num()]
        print(f"Compare A: {entry_a['name']}, {entry_a['description']}, from {entry_a['country']}.")

    print(vs)
    entry_b = data[rand_num()]
    print(f"Compare B: {entry_b['name']}, {entry_b['description']}, from {entry_a['country']}.")

    answer = input('Who has more followers? Type \'A\' or \'B\': ').lower()
    follower_list = compare(entry_a['follower_count'], entry_b['follower_count'])
    if answer == 'b':
        if entry_b['follower_count'] == follower_list[1]:
            score += 1
            os.system('clear')
            print(f'You got it right! Current score {score}')
        else:
            os.system('clear')
            print(f'Sorry, you got it wrong! Final score {score}')
            game_over = True
    elif answer == 'a':
        if entry_a['follower_count'] == follower_list[1]:
            score += 1
            os.system('clear')
            print(f'You got it right! Current score {score}')
        else:
            os.system('clear')
            print(f'Sorry you got it wrong! Final score {score}')
            game_over = True