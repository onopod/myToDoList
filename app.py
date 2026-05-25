from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "こんにちは"


@app.route("/add")
def add():
    if # POSTで飛んで来たら:
        # フォームの内容チェック
        if # 正しければ:
            # insert
            # 詳細画面にリダイレクト
        