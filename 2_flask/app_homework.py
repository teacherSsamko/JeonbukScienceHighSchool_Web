from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<html><body><h1>Hello, World!</h1><a href='/post'>포스트 보러가기</a></body></html>"


@app.route("/about")
def about():
    return "<html><body><h1>About Page</h1><p>This is the about page.</p></body></html>"


@app.route("/post")
def post():
    return """<html>
    <body>
    <h1>Post</h1>
    <h2>전북과학고 웹서버 만들기</h2>
    <p>작성자: 이은섭 | 날짜: 24.08.05</p>
    <p>Flask를 이용해 웹 서버를 만들어봅시다.</p>
    <a href="/">홈으로 가기</a>
    </body>
    </html>"""


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
