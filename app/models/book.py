import enum
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db

class BookStatus(enum.Enum):
  WANT_TO_READ = 'want_to_read'
  CURRENTLY_READING = 'currently_reading'
  READ = 'read'
  DID_NOT_FINISH = 'did_not_finish'

class Book(db.Model):
  __tablename__ = "books"
  
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  google_books_id: Mapped[str] = mapped_column(nullable=False)
  title: Mapped[str] = mapped_column(nullable=False)
  author: Mapped[str] = mapped_column(nullable=False)
  # identifier: Mapped[int] = mapped_column()
  imageUrl: Mapped[str] = mapped_column(nullable=False)
  status: Mapped[BookStatus]= mapped_column(Enum(BookStatus), nullable=True)
