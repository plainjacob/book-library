from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db
from app.models.book_authors import BookAuthors


class Author(db.Model):
  __tablename__ = "authors"
  
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(nullable=False, unique=True)
  books: Mapped[list['Book']] = relationship(secondary=BookAuthors.__table__, back_populates='authors')