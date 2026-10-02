from flask import request, redirect, url_for
from app.api import api_bp
from app.extensions import db
from app.services.google_books import get_book_by_id
from app.models import Book


@api_bp.route('/add-book', methods=['POST'])
def add_book():
  data = request.get_json()
  google_books_id = data.get('google_books_id')
  book = get_book_by_id(google_books_id)
  db.session.add(book)
  db.session.commit()

  return {'message': 'Book added successfully.'}


@api_bp.route('/delete-book', methods=['POST'])
def delete_book():
  data = request.get_json()
  id = data.get('id')
  book = db.get_or_404(Book, id)
  db.session.delete(book)
  db.session.commit()

  return {'message': 'Book deleted successfully'}