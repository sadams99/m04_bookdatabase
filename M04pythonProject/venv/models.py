from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Book(db.Model):
    id = db.column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(100),nullable = False)
    author = db.Column(db.String(100),nullable = False)
    publisher = db.Column(db.String(100), nullable = True)
    
    def as_dist(self):
        return{
            "id" : self.id,
            "book" : self.book_name,
            "author": self.author,
            "publisher": self.publisher
        }