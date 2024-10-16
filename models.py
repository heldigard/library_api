from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)
    author = db.relationship('Author', backref=db.backref('books', lazy=True))
    category = db.relationship('Category', backref=db.backref('books', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author.name,
            "category": self.category.name,
            "publication_year": self.publication_year,
            "available_copies": self.available_copies
        }