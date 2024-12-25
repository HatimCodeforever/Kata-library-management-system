from sqlalchemy import create_engine, Column, String, Integer, Boolean, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import expression
import datetime

# Database setup
DATABASE_URL = "sqlite:///library.db"  # SQLite database for development
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Book model with added constraints
class Book(Base):
    __tablename__ = "books"
    
    id = Column(String(13), primary_key=True)  # ISBN: 13 characters
    title = Column(String(100), nullable=False)  # Title with max length 100
    author = Column(String(100), nullable=False)  # Author with max length 100
    year = Column(Integer, nullable=False)  # Year should be between 1800 and current year
    available = Column(Boolean, default=True)  # Default value for availability is True

    __table_args__ = (
        CheckConstraint(year >= 1800, name="year_gte_1800"),  # Ensure year is >= 1800
        CheckConstraint(year <= datetime.datetime.now().year, name="year_lte_current_year"),  # Ensure year is <= current year
    )

# Create the database tables
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
