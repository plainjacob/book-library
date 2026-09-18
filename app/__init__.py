from flask import Flask, render_template
from app.extensions import db

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

  db.init_app(app)

  @app.route('/')
  def index():
    return render_template('index.html', title='My Library')

  return app
