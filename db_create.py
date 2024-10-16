import json
from app import db, app  # Import db and app from your app.py
from models import Book, Author, Category

def create_db_and_load_data():
    with app.app_context():
        db.create_all()

        try:
            with open('data.json', 'r') as f:
                data = json.load(f)

            for author_data in data['authors']:
                author = Author(name=author_data['name'])
                db.session.add(author)

            for category_data in data['categories']:
                category = Category(name=category_data['name'])
                db.session.add(category)

            db.session.commit()  # Commit authors and categories first

            # Now add books (needs IDs of authors and categories)
            for book_data in data['books']:
                author = Author.query.filter_by(name=book_data['author']).first()
                category = Category.query.filter_by(name=book_data['category']).first()

                if author and category:  # Only add if author and category exist
                    # Check if the book already exists
                    existing_book = Book.query.filter_by(isbn=book_data['isbn']).first()
                    if not existing_book:
                        book = Book(
                            isbn=book_data['isbn'],
                            title=book_data['title'],
                            author_id=author.id,
                            category_id=category.id,
                            publication_year=book_data['publication_year'],
                            available_copies=book_data['available_copies']
                        )
                        db.session.add(book)
            db.session.commit()

        except Exception as e:
            print(f"Error creating database and loading data: {e}")
            db.session.rollback()

if __name__ == '__main__':
    create_db_and_load_data()