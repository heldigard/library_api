from flask import jsonify
from app import app

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "status": 404}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "status": 400}), 400

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error", "status": 500}), 500