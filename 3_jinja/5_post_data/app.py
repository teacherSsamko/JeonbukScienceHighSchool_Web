from flask import Flask, render_template

app = Flask(__name__)

post_data = {
    "title": "블로그 만들기",
    "author": "이은섭",
    "date": "2024-08-06",
    "content": "오늘은 Flask로 블로그를 만들어보았다.",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/post")
def post():
    return render_template("post.html", post=post_data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
