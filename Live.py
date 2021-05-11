from GuessGame import play as play_guess
from MemoryGame import play as play_memory
from CurrencyRouletteGame import play as play_currency
from Helpers import in_range
from Scores import clear_score
from Scores import add_score
from Utils import screen_cleaner


def welcome():
    screen_cleaner()
    clear_score()
    name = input("What is your name? ")
    # Check if valid name
    while not all(char.isalpha() for char in name) or not len(name) > 1:
        name = input("That ain't no name. What's your real name? ")
    return "Hello " + name.capitalize() + " and welcome to the World of Games(WOG).\n\
Here you can find many cool games to play."


def play_game(game_number, difficulty):
    if game_number == 1:
        return play_memory(difficulty)
    elif game_number == 2:
        return play_guess(difficulty)
    elif game_number == 3:
        return play_currency(difficulty)


def play_again():
    answer = ""
    while answer != "yes" or answer != "no":
        answer = input("Would you like to play another game? (type yes or no) ")
        if answer == "yes":
            return True
        elif answer == "no":
            print("Thank you for playing.")
            return False


def load_game():
    playing = True
    while playing:
        game = input("Please choose a game to play:\n \
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n \
        2. Guess Game - guess a number and see if you chose like the computer \n \
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n \
        Your choice: ")

        # Choose game within range
        game_number = in_range(game, 1, 4)

        level = input("Please choose game difficulty from 1 to 5: ")

        # Choose difficulty within range
        level_number = in_range(level, 1, 6)
        game_result = play_game(game_number, level_number)
        if game_result:
            add_score(level_number)
        playing = play_again()
