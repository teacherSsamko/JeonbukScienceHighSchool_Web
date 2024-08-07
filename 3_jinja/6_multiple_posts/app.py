from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "title": "웹서버 개념",
        "author": "이은섭",
        "date": "2024-08-05",
        "content": "오늘은 웹 서버의 개념에 대해 알아보았다.",
    },
    {
        "title": "블로그 만들기",
        "author": "이은섭",
        "date": "2024-08-06",
        "content": "오늘은 Flask로 블로그를 만들어보았다.",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts/<int:post_id>")
def post(post_id):
    post_data = posts[post_id - 1]
    return render_template("post.html", post=post_data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
