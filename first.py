print('Rock Paper Scissors!!')
choices = ['rock', 'paper', 'scissors']

import random
def get_comp_choice():
    return choices[random.randint(0, 2)]

def play(comp, user):
    if user + comp == 'paperscissors':
        print('comp beats user with scissors')
    elif user + comp == 'paperrock':
        print('user beats comp with paper')
    elif user + comp == 'rockpaper':
        print('comp beats user with paper')
    elif user + comp == 'rockscissors':
        print('user beats comp with rock')
    elif user + comp == 'scissorsrock':
        print('comp beats user with rock')
    elif user + comp == 'scissorspaper':
        print('user beats comp with scissors')
    else:
        print("It's a tie")


num_of_times = list(range(10))
index = -1
for num in num_of_times:
    user_choice = raw_input('Choose your weapon: ')
    play(get_comp_choice(), user_choice)
    num_of_times.append(num_of_times[index] + 1)
