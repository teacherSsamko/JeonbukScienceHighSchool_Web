from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    "삶이 있는 한 희망은 있다. - 키케로",
    "산다는것 그것은 치열한 전투이다. - 로망로랑",
    "하루에 3시간을 걸으면 7년 후에 지구를 한바퀴 돌 수 있다. - 사무엘존슨",
    "언제나 현재에 집중할수 있다면 행복할것이다. - 파울로 코엘료",
    "진정으로 웃으려면 고통을 참아야하며, 나아가 고통을 즐길 줄 알아야 해. - 찰리 채플린",
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/random_quote")
def random_quote():
    return jsonify(random.choice(quotes))


if __name__ == "__main__":
    app.run(debug=True)
