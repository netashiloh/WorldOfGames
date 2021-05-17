from Utils import SCORES_FILE_NAME
from flask import Flask, redirect, url_for


def get_txt_content():
    my_file = open(SCORES_FILE_NAME, "r")
    current_score = my_file.readline()
    return int(current_score)


def score_server(score):
    app = Flask(__name__)

    @app.route("/")
    def home():
        return f"""<html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <h1>The score is <div id="score">{score}</div></h1>
    </body>
    </html>"""

    @app.route("/<name>")
    def user(name):
        return f"No such page: {name}!"

    @app.route("/admin")
    def admin():
        return redirect(url_for("home"))

    if __name__ == "__main__":
        app.run()


def score_web():
    score = get_txt_content()
    score_server(score)


score_web()
