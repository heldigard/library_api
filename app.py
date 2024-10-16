from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Importa las rutas divididas
from routes.book_routes import *
from routes.author_routes import *
from routes.category_routes import *

if __name__ == '__main__':
    with app.app_context():  # create tables with app context
        db.create_all()  # create tables
    app.run(debug=True)