import random
from time import sleep
import os
from Helpers import integer_check


def generate_sequence(difficulty):
    # generate numbers in accordance to difficulty
    generated_numbers = []
    i = 0
    while i < difficulty:
        number = random.randrange(1, 101)
        generated_numbers.append(number)
        i += 1
    return generated_numbers


def show_sequence(x):
    print(x)
    sleep(5)
    if os.name == 'nt':
        os.system('clear')
    else:
        os.system('cls')


def get_list_from_user(difficulty):
    list_from_user = []
    i = 0
    print("Do you remember the sequence?")
    while i < difficulty:
        player_input = input("What is number " + str(i+1) + "? ")
        number = integer_check(player_input)
        list_from_user.append(int(number))
        i += 1
    return list_from_user


def is_list_equal(x, y):
    if x == y:
        print("You won!")
    else:
        print("Nice try.\nMaybe next time...")


def play(difficulty):
    x = generate_sequence(difficulty)
    show_sequence(x)
    y = get_list_from_user(difficulty)
    is_list_equal(x, y)
