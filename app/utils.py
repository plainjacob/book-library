import json
from app.extensions import db
from app.models import Book, Author


def get_sample_data():
  with open("sample_data.json", "r") as f:
    data = json.load(f)

  books = []
  for book in data['items']:
    info = book['volumeInfo']

    authors = []
    names: list = info.get('authors', [])
    for name in names:
      # If author is already in database: Get that database object, and put it in list instead of making a new author object.
      author = db.session.execute(db.select(Author).filter_by(name=name)).scalar_one_or_none()
      if author is None:
        author = Author(
          name=name
        )
      authors.append(author)
  
    book = Book(
      google_books_id=book.get('id'),
      title=info.get('title'),
      authors=authors,
      imageUrl=info.get('imageLinks', {}).get('thumbnail'),
      status=None
    )
    books.append(book)

  return books
