import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book

# Simulated return_book function
def return_book(book_id, session):
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        raise ValueError("Book not found.")
    if book.available:
        raise ValueError("Book is already available.")
    book.available = True
    session.commit()

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database
        self.engine = create_engine("sqlite:///:memory:")
        # Create all tables defined in the Base class
        Base.metadata.create_all(self.engine)
        # Create a session to interact with the database
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Insert initial data for testing
        book = Book(id="1234567890129", title="Sample Book", author="Sample Author", year=2023, available=False)
        self.session.add(book)
        self.session.commit()

    def tearDown(self):
        # Close the session and drop all tables
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_return_book(self):
        # Return the borrowed book
        return_book("1234567890129", self.session)

        # Query the book and assert that it is now available
        book = self.session.query(Book).filter_by(id="1234567890129").first()
        self.assertTrue(book.available)

    def test_return_book_that_is_already_available(self):
        # Try to return a book that's already available
        return_book("1234567890129", self.session)
        with self.assertRaises(ValueError):
            return_book("1234567890129", self.session)
            
    def test_return_non_existent_book(self):
        # Try to return a non-existent book
        with self.assertRaises(ValueError):
            return_book("non_existent_id", self.session)

if __name__ == "__main__":
    unittest.main()
