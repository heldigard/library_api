from flask import jsonify, request, abort
from app import db, cache, app
from models import Category

@app.route('/categories', methods=['GET'])
@cache.cached(timeout=60)
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get_or_404(category_id)
    return jsonify(category.to_dict())

@app.route('/categories', methods=['POST'])
def create_category():
    new_category = request.get_json()
    category = Category(**new_category)
    db.session.add(category)
    db.session.commit()
    return jsonify(category.to_dict()), 201

@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    updated_data = request.get_json()
    for key, value in updated_data.items():
        setattr(category, key, value)
    db.session.commit()
    return jsonify(category.to_dict())

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return '', 204