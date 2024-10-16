from flask import jsonify, request, abort
from app import db, cache, app
from models import Author

@app.route('/authors', methods=['GET'])
@cache.cached(timeout=60)
def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors])

@app.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get_or_404(author_id)
    return jsonify(author.to_dict())

@app.route('/authors', methods=['POST'])
def create_author():
    new_author = request.get_json()
    author = Author(**new_author)
    db.session.add(author)
    db.session.commit()
    return jsonify(author.to_dict()), 201

@app.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    author = Author.query.get_or_404(author_id)
    updated_data = request.get_json()
    for key, value in updated_data.items():
        setattr(author, key, value)
    db.session.commit()
    return jsonify(author.to_dict())

@app.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    return '', 204