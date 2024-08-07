from flask import Flask, render_template

app = Flask(__name__)

# 예시 블로그 포스트 데이터
posts = [
    {
        "title": "첫 번째 포스트",
        "author": "학생 A",
        "content": "이것은 첫 번째 블로그 포스트의 내용입니다.",
        "date_posted": "2024-07-24",
    },
    {
        "title": "두 번째 포스트",
        "author": "학생 B",
        "content": "이것은 두 번째 블로그 포스트의 내용입니다.",
        "date_posted": "2024-07-25",
    },
]


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = posts[post_id - 1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
