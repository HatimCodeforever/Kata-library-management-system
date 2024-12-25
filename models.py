from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup
DATABASE_URL = "sqlite:///library.db"  # SQLite database for development
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Book model
class Book(Base):
    __tablename__ = "books"
    id = Column(String, primary_key=True)  # Unique identifier for each book
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)  # True if the book is available

# Create the database tables
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
