import os

from dotenv import load_dotenv

load_dotenv()


class Config():
  SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
  SECRET_KEY = os.getenv("SECRET_KEY")
  GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")


config = Config()