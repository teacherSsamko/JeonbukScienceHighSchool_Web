from flask import Flask, request, jsonify

app = Flask(__name__)

books = []


@app.route("/books", methods=["GET", "POST"])
def manage_books():
    if request.method == "GET":
        return jsonify(books)

    if request.method == "POST":
        new_book = request.get_json()
        if new_book is None:
            return {"message": "Invalid JSON format"}, 400
        books.append(new_book)
        return new_book, 201


@app.route("/books/<int:book_id>", methods=["GET", "PUT", "DELETE"])
def manage_single_book(book_id):
    global books
    if request.method == "GET":
        for book in books:
            if book["id"] == book_id:
                return jsonify(book)
        return {"message": "Book not found"}, 404

    if request.method == "PUT":
        for book in books:
            if book["id"] == book_id:
                updated_data = request.get_json()
                book.update(updated_data)
                return jsonify(book)
        return {"message": "Book not found"}, 404

    if request.method == "DELETE":
        books = [book for book in books if book["id"] != book_id]
        return {"message": "Book deleted"}, 200


if __name__ == "__main__":
    app.run(debug=True)
