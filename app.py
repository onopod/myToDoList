from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "こんにちは"

@app.route("/detail")
def detail():
    return "詳細画面"