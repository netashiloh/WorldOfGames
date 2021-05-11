import random
from Helpers import in_range


def difficulty_level(difficulty):
    return difficulty * 5


def generate_number(level):
    return random.randrange(1, level+1)


def get_guess_from_user(level):
    guess = input("Please choose a number between 1 to " + str(level) + ": ")
    guess = in_range(guess, 1, level+1)
    return guess


def compare_results(x, y):
    if x == int(y):
        print("DingDingDing! You won.")
        return True
    else:
        print("*BUZZER* No,"
              "The number was " + str(x) + ".")
        return False


def play(difficulty):
    level = difficulty_level(difficulty)
    x = generate_number(level)
    y = get_guess_from_user(level)
    result = compare_results(x, y)
    return result
