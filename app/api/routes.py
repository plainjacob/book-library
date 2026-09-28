from flask import request
from app.api import api_bp
from app.extensions import db
from app.services.google_books import get_book_by_id


@api_bp.route('/api/add_book', methods=['POST'])
def add_book():
  data = request.get_json()
  google_books_id = data.get('google_books_id')
  book = get_book_by_id(google_books_id)
  db.session.add(book)
  db.session.commit()

  return {'message': 'Success'}