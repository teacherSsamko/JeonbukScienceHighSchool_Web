from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

feedbacks = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        feedbacks.append({"name": name, "message": message})
        return redirect(url_for("index"))
    return render_template("feedback.html")


@app.route("/feedbacks")
def show_feedbacks():
    return render_template("show_feedbacks.html", feedbacks=feedbacks)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
