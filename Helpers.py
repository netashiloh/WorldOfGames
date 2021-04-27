def integer_check(player_input):
    while True:
        try:
            # Convert it into integer
            test = int(player_input)
        except ValueError:
            print("Input is not a number. input = ", player_input)
            player_input = input("Please choose an integer:")
            continue
        else:
            return player_input


def in_range(player_input, x, y):
    # Checking if int & in range of choices
    while int(integer_check(player_input)) not in range(x, y):
        player_input = input("Please choose from the existing options: " + str(x) + ", " + str(y-1) + ".")

    return int(player_input)

# def integer_check(player_input):
#     while True:
#         try:
#             # Convert it into integer
#             test = int(player_input)
#         except ValueError:
#             player_input = input("Please choose a number: ")
#             continue
#         else:
#             return test

# def integer_check(user_input):
#     while not str(user_input).isnumeric():
#         try:
#             user_input = int(input('Enter a number: '))
#             break
#         except ValueError:
#             print('Please enter a valid number: ')
#     return str(user_input)
#

# def integer_check(user_input):
#     while not str(user_input).isnumeric():
#         user_input = input("Enter a number: ")
#     return int(user_input)


