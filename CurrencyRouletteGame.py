import random
from Helpers import integer_check
from openexchangerate import OpenExchangeRates


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
    # define api and api key
    client = OpenExchangeRates(api_key="873650114a6e43e8b46644757901d1fc")
    # Get the latest foreign exchange rates from USD to ILS
    latest_conversions = (client.latest()[0])
    # Get the latest ILS rate
    ils_value = latest_conversions['ILS']

    # convert (get exchange rate of given value)
    return ils_value * value


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


play(1)