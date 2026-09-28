from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db


class BookAuthors(db.Model):
  __tablename__ = "book_authors"
  
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
  author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))