from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<html><body><h1>Hello, World!</h1></body></html>"


@app.route("/about")
def about():
    return "<html><body><h1>About Page</h1><p>This is the about page.</p></body></html>"


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
