import json
from app.models.book import Book


def get_sample_data():
  with open("sample_data.json", "r") as f:
    data = json.load(f)

  books = []
  for book in data['items']:
    info = book['volumeInfo']
  
    book = Book(
      google_books_id=book.get('id'),
      title=info.get('title'),
      author=info.get('authors', []),
      imageUrl=info.get('imageLinks', {}).get('thumbnail'),
      status=None
    )
    books.append(book)

  return books
