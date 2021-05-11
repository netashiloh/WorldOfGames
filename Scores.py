from Utils import SCORES_FILE_NAME


def clear_score():
    my_file = open(SCORES_FILE_NAME, "w")
    my_file.write("0")
    my_file.close()


def add_score(difficulty):
    my_file = open(SCORES_FILE_NAME, "r+")
    current_score = my_file.readline()
    new_score = (difficulty * 3 + 5) + int(current_score)
    my_file.seek(0)
    my_file.truncate()
    my_file.write(str(new_score))
    my_file.close()


add_score(5)
