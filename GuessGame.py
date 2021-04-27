import random
from Helpers import in_range


def difficulty_level(difficulty):
    return difficulty * 5


def generate_number(level):
    return random.randrange(1, level)


def get_guess_from_user(level):
    guess = input("Please choose a number between 1 to " + str(level) + ": ")
    guess = in_range(guess, 1, level)
    return guess


def compare_results(x, y):
    if x == int(y):
        return True
    else:
        return False


def play(difficulty):
    level = difficulty_level(difficulty)
    x = generate_number(level)
    y = get_guess_from_user(level)
    if compare_results(x, y):
        print("DingDingDing! You won.")
    else:
        print("*BUZZER* No. "
              "The number was " + str(x) + ".")
