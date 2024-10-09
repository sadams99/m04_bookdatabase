from flask import Flask, request, jsonify, render_template
from models import db, Book

app = (
    Flask(__name__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://books.db"
app.comfig["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app.context():
    db.create_all()
    
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/books", methods = ["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([books.as_dict() for books in books])

@app.route("/books/<int:book_id>", methods = ["GET"])
def get_book(book_id):
    book = Book.query.get(book_id)
    return jsonify(book.as_dict())

@app.route("/books", methods = ["POST"])
def add_book():
    new_book: request.get_json()
    book = Book(
        book_name = new_book["book_name"],
        author = new_book["author"],
        publisher = new_book["publisher"],
    )
    db.session.add(Book)
    db.session.commit()
    return jsonify(book.as_dict()), 201

@app.route("/books/<int:book_id>", methods = ["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    updated_data: request.get_json()
    book.book_name = updated_data["book_name"]
    book.author = updated_data["author"]
    book.publisher = updated_data["publisher"]
    db.session.commit()
    return jsonify(book.as_dict())

@app.route("/books/<int:book_id>", methods = ["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message" : "book deleted"})

if __name__ == "__main__":
    app.run(debug=True)
