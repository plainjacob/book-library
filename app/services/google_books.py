import requests
from app.config import config
from app.models import Author, Book

def search_books(query):
  url = 'https://www.googleapis.com/books/v1/volumes'
  params = {
            'q': query,
            'maxResults': 10,
            'key': config.GOOGLE_BOOKS_API_KEY
          }
  
  response = requests.get(url, params=params)
    
  data = response.json()

  books = []
  authors = []
  for book in data['items']:
    info = book['volumeInfo']

    names: list = info.get('authors')
    for name in names:
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

def get_book_by_id(google_books_id):
  url = f'https://www.googleapis.com/books/v1/volumes/{google_books_id}'
  params = {
    'key': config.GOOGLE_BOOKS_API_KEY
  }
  response = requests.get(url, params=params)

  data = response.json()

  info = data['volumeInfo']

  authors = []
  names: list = info.get('authors')
  for name in names:
    author = Author(
      name=name
    )
    authors.append(author)

  book = Book(
    google_books_id=data.get('id'),
      title=info.get('title'),
      authors=authors,
      imageUrl=info.get('imageLinks', {}).get('thumbnail'),
      status=None
  )
  return book
