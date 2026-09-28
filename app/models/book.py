import enum
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship, WriteOnlyMapped
from app.extensions import db
from app.models.book_authors import BookAuthors

class BookStatus(enum.Enum):
  WANT_TO_READ = 'want_to_read'
  CURRENTLY_READING = 'currently_reading'
  READ = 'read'
  DID_NOT_FINISH = 'did_not_finish'


class Book(db.Model):
  __tablename__ = "books"
  
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  google_books_id: Mapped[str] = mapped_column(nullable=False, unique=True)
  title: Mapped[str] = mapped_column(nullable=False)
  imageUrl: Mapped[str] = mapped_column(nullable=False)
  status: Mapped[BookStatus]= mapped_column(Enum(BookStatus), nullable=True)
  authors: Mapped[list['Author']] = relationship(secondary=BookAuthors.__table__, back_populates='books')