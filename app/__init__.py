from flask import Flask, render_template
from app.config import config
from app.extensions import db
from app.models.book import Book
from app.forms import SearchBookForm
from app.services.google_books import search_books
from app.utils import get_sample_data


def create_app():
  app = Flask(__name__)
  app.config.from_object(config)

  db.init_app(app)

  @app.route('/')
  def index():
    books = db.session.execute(db.select(Book))
    return render_template('index.html', title='My Library', books=books)

  @app.route('/search', methods=['GET', 'POST'])
  def search():
    form = SearchBookForm()
    if form.validate_on_submit():
      if form.title.data:
        books = get_sample_data()
        # books = search_books(form.title.data)
        
    return render_template('search_book.html', title='Search Book', form=form, books=books)

  return app


from app import models