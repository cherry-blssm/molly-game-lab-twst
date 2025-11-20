import random
import time

from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    username = input('Name: ')

    print_dramatic_text ('Welcome, ' + username + '!')
    answer = input('Please imput your password: ')
    if answer.lower() == 'love':
        print_dramatic_text('Correct!!')
    else:
        print_dramatic_text('Uh oh!!')

    answer = input('HINT - Romantic Feeling ')
    while answer.lower() != 'love':
        print_dramatic_text('Uh oh ...')
        answer = input('Try again!! HINT - Romantic Feeling ')
    print_dramatic_text('Correct!!')
    answer = input('HINT - Laugh Out Loud!! ')
    while answer.lower() != 'lol':
        print_dramatic_text('Uh oh ...')
        answer = input('Try again!! HINT - Laugh Out Loud!! ')
    print_dramatic_text('Correct!!')
    answer = input('HINT - That Number. ')
    while answer != '67':
        print_dramatic_text('Uh oh ...')
        answer = input('Try again!! HINT - That Number. ')
    print_dramatic_text('Correct!!')
    answer = input('HINT - Disney princess with hair for days ')
    while answer.lower() != 'rapunzel':
        print_dramatic_text('Uh oh ...')
        answer = input('Try again!! HINT - Disney princess with hair for days ')
    print_dramatic_text('Correct!!')
    answer = input('HINT - One of the series on a poster in Mr Mazeys room ')
    while answer.lower() != 'deathnote':
        print_dramatic_text('Uh oh ...')
        answer = input('Try again!! HINT - One of the series on a poster in Mr Mazeys room ')
    print_dramatic_text('Correct!!')
    answer = input('HINT - What is the prize for this presentation? ')
    while answer.lower() != 'labubu':
        print_dramatic_text('Uh oh ...')
        answer = input('Try again!! HINT - What is the prize for this presentation? ')
    print_dramatic_text('Correct!!')
    answer = input('HINT - How old am I? ')
    while answer != '15':
        print_dramatic_text('Uh oh ...')
        answer = input('Try again!! HINT - How old am I? ')
    print_dramatic_text('Correct!!')
    answer = input('HINT - PUT IT ALL TOGETHER!! ')
    while answer.lower() != 'lovelol67rapunzeldeathnotelabubu15':
        print_dramatic_text('Uh oh ...')
        answer = input('Try again!! HINT - Every answer, no spaces!! ')
    print_dramatic_text('CONGRADULATIONS!!')

    print ("""
           ⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠶⠒⠶⠾⠷⠖⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣣⠶⠶⢤⡀⣠⣤⣄⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢳⡏⠀⠀⠈⠿⠅⠀⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⣤⣄⣀⠀⠀⣼⠏⠘⣧⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢾⣷⣦⠀⠈⢷⣄⠀⢀⣠⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢧⡀⠀⠀⣹⣿⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠈⢹⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡗⠀⢀⡟⠀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣦⣄⠀⠀⠀⠀⣸⠃⠀⣼⠁⣼⢨⣵⣦⢢⣀⣀⡀⡀⠀⠀⢠⠞⠋⠙⢳⡄⠀
⠀⢀⡶⣛⣛⠳⣆⣀⣀⣠⣤⣤⠤⠾⢳⣿⣿⣾⢷⠀⠀⢰⡏⠀⠀⣏⢰⠇⠹⢿⠿⠃⠉⢉⣍⣉⡙⠛⠛⠰⣿⣿⡟⣧⠀
⠀⢸⡗⣿⣿⡿⠀⣤⣀⣠⡄⠀⠀⠀⠀⠙⠛⠁⢸⡄⢠⡏⠀⠀⠀⢿⡿⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠈⠁⠀⣿⠀
⠀⠀⡇⠀⠀⠀⠀⠛⠥⠖⠃⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣤⡀⠀⠀⢸⡟⣦⡴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢿⠀
⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣟⠁⠀⠀⣾⠛⠋⢀⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠹⣆⢸⡀
⢿⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠘⠧⠀⠀⣿⠀⠀⠛⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⠀⠀⢸⡇
⠠⠑⠼⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠁⠟⠃⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⢸⡇⠀⠀⢰⡇⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⣯⠀⠀⠀⣠⣤⠴⠶⠶⠶⠾⠛⠛⠋⠉⠙⠳⠤⠞⠃⠀⠀⠈⠻⠶⠞⠋⠉⠉⠉⠉⠉⠉⠉⠙⠛⠛⢷⡆⠀⢀⣼⠃
⠀⠀⠑⠲⠠⠜⠁⠤⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠳⠖⠋⠁⠀
           """)

    print ('THANKS FOR PLAYING!!')