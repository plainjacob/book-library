import enum
from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BookStatus(enum.Enum):
  WANT_TO_READ='want_to_read'
  CURRENTLY_READING='currently_reading'
  READ='read'
  DID_NOT_FINISH='did_not_finish'

class Book(Base):
  __tablename__ = "books"
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String, nullable=False, unique=True)
  status = Column(Enum(BookStatus), nullable=False)

engine = create_engine('sqlite:///books.db')

Base.metadata.create_all(engine)

def recreate_db():
  Base.metadata.drop_all(engine)
  Base.metadata.create_all(engine)