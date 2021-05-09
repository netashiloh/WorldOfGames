import random
from Helpers import integer_check
from tests import ILS_value


def describe_game():
    print("Welcome to Currency Roulette Game!\n"
          "This game is simple: We will convert a value of money from USD to ILS.\n"
          "The difficulty you chose will determine the range of your guess for the correct answer.\n"
          "Ready? Here we go!")


def value_of_money():
    value = random.randrange(1, 101)
    return value


def get_money_interval(converted_value, difficulty):
    start = int(converted_value - (5 - difficulty))
    end = int((converted_value + (5 - difficulty)))

    return start, end


def get_exchange_rate(value):
    #api = Api()
    # Get the latest foreign exchange rates from USD to ILS
    #api.get_rates()
    # convert (get exchange rate of given value)
    return ILS_value * value


def get_guess_from_user(value):
    player_input = input("How many ILS will be " + str(value) + " USD? ")
    return int(integer_check(player_input))


def compare_guess_with_converted_value(player_input, interval):
    if player_input in range(interval[0], interval[1]+1):
        print("You won!")
    else:
        print("You suck.")


def play(difficulty):
    describe_game()
    value = value_of_money()
    converted_value = get_exchange_rate(value)
    player_input = get_guess_from_user(value)
    compare_guess_with_converted_value(player_input, get_money_interval(converted_value, difficulty))