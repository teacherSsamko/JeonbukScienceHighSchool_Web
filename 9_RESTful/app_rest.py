from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = []


class Book(Resource):
    def get(self, book_id=None):
        if book_id is None:
            return jsonify(books)
        for book in books:
            if book["id"] == book_id:
                return jsonify(book)
        return {"message": "Book not found"}, 404

    def post(self):
        new_book = request.get_json()
        if new_book is None:
            return {"message": "Invalid JSON format"}, 400
        books.append(new_book)
        return new_book, 201

    def put(self, book_id):
        for book in books:
            if book["id"] == book_id:
                updated_data = request.get_json()
                book.update(updated_data)
                return jsonify(book)
        return {"message": "Book not found"}, 404

    def delete(self, book_id):
        global books
        books = [book for book in books if book["id"] != book_id]
        return {"message": "Book deleted"}, 200


api.add_resource(Book, "/books", "/books/<int:book_id>")

if __name__ == "__main__":
    app.run(debug=True)
