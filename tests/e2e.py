from selenium import webdriver
import os


def check_os():
    if os.name == 'nt':
        my_driver = webdriver.Chrome(executable_path="./chromedriver_windows.exe")
    else:
        my_driver = webdriver.Chrome(executable_path="./chromedriver")

    return my_driver


def test_scores_service(my_driver):
    my_driver.get("http://127.0.0.1:8777/")
    web_score = my_driver.find_element_by_id("score").text
    my_driver.quit()
    if int(web_score) in range(1, 1001):
        return True
    else:
        return False


def main_function():
    my_driver = check_os()
    if test_scores_service(my_driver):
        return 0
    else:
        return -1


print(main_function())

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')




