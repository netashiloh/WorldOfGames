from flask import Flask, redirect, url_for

app = Flask(__name__)
score=80


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
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()