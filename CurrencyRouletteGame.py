# import random
# from exchangeratesapi import Api
# from Helpers import integer_check


def describe_game():
    print("Welcome to Currency Roulette Game!\n"
          "This game is simple: We will convert a value of money from USD to ILS.\n"
          "The difficulty you chose will determine the range of your guess for the correct answer.\n"
          "Ready? Here we go!")


def value_of_money():
    value = random.randrange(1, 101)
    return value


def get_money_interval(difficulty, converted_value):
    money_interval = (converted_value - (5 - difficulty), converted_value + (5 - difficulty))
    return money_interval


def get_exchange_rate(value):
    api = Api()
    # Get the latest foreign exchange rates from USD to ILS
    api.get_rates()
    # convert (get exchange rate of given value)
    return converted_value


def get_guess_from_user(value):
    player_input = input("How many ILS will be " + value + "? ")
    return integer_check(player_input)


def compare_guess_with_value_convert(x, y):
    pass


def play(difficulty):
    # describe_game()
    # value = value_of_money()
    # get_money_interval(value, difficulty)
    # converted_value = get_exchange_rate(value)
    # player_input = get_guess_from_user(value)
    # compare_guess_with_converted_value(player_input, converted_value)
    print("Sorry! This game is not ready.")
