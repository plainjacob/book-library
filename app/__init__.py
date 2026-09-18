from flask import Flask, render_template
from app.extensions import db
from app.models.book import Book

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

  db.init_app(app)

  @app.route('/')
  def index():
    books = db.session.execute(db.select(Book))
    return render_template('index.html', title='My Library', books=books)

  return app


from app import models