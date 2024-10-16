from flask import jsonify, request, abort
from app import db, cache, app
from models import Book, Author, Category

@app.route('/books', methods=['GET'])
@cache.cached(timeout=60)
def get_books():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    author = request.args.get('author')
    category = request.args.get('category')
    title = request.args.get('title')

    query = Book.query
    if author:
        query = query.join(Author).filter(Author.name.ilike(f'%{author}%'))
    if category:
        query = query.join(Category).filter(Category.name.ilike(f'%{category}%'))
    if title:
        query = query.filter(Book.title.ilike(f'%{title}%'))

    books = query.paginate(page=page, per_page=per_page, error_out=False).items
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    book = Book(**new_book)
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    updated_data = request.get_json()
    for key, value in updated_data.items():
        setattr(book, key, value)
    db.session.commit()
    return jsonify(book.to_dict())

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204