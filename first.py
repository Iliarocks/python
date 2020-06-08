print('Rock Paper Scissors!!')
user = raw_input('Choose your weapon: ')
choices = ['rock', 'paper', 'scissors']

import random
def get_comp_choice():
    return choices[random.randint(0, 2)]

def play(comp):
    print(user + comp)
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

play(get_comp_choice())
