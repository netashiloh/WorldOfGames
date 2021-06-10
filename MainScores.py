from Utils import SCORES_FILE_NAME
from flask import Flask


def score_server():
    app = Flask(__name__)

    @app.route("/")
    def home():
        try:
            my_file =open(SCORES_FILE_NAME, "r")
            score = my_file.readline()
            return f"""<html>
                    <head>
                    <title>Scores Game</title>
                    </head>
                    <body>
                    <h1>The score is <div id="score">{score}</div></h1>
                    </body>
                    </html>"""
        except BaseException as error:
            return f"""<html>
                    <head>
                    <title>Scores Game</title>
                    </head>
                    <body>
                    <body>
                    <h1><div id="score" style="color:red">{error}</div></h1>
                    </body>
                    </html>"""

    @app.route("/<name>")
    def user(name):
        return f"No such page: {name}!"

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8777)


score_server()
