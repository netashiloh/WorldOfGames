from selenium import webdriver


def test_scores_service():
    my_driver = webdriver.Chrome(executable_path="./chromedriver")
    my_driver.get("http://127.0.0.1:8777/")
    web_score = my_driver.find_element_by_id("score").text
    my_driver.quit()
    if int(web_score) in range(1, 1001):
        return True
    else:
        return False


def main_function():
    if test_scores_service():
        return 0
    else:
        return -1


print(main_function())





