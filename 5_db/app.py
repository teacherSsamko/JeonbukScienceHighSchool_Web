from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# 데이터베이스 초기화
def init_db():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS todos
        (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, done BOOLEAN)"""
    )
    conn.commit()
    conn.close()


# 애플리케이션 실행 시 데이터베이스 초기화
init_db()


@app.route("/")
def index():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    todos = c.fetchall()
    conn.close()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["GET", "POST"])
def add_todo():
    if request.method == "POST":
        task = request.form["task"]
        conn = sqlite3.connect("todo.db")
        c = conn.cursor()
        c.execute("INSERT INTO todos (task, done) VALUES (?, ?)", (task, False))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("add_todo.html")


@app.route("/update/<int:todo_id>", methods=["GET", "POST"])
def update_todo(todo_id):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    todo = c.fetchone()
    conn.close()
    if request.method == "POST":
        task = request.form["task"]
        done = request.form.get("done") == "on"
        conn = sqlite3.connect("todo.db")
        c = conn.cursor()
        c.execute(
            "UPDATE todos SET task = ?, done = ? WHERE id = ?", (task, done, todo_id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("update_todo.html", todo=todo)


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
