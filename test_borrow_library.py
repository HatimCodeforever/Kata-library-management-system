import unittest
from models import Book, Session

class TestLibraryManagement(unittest.TestCase):
    def setUp(self):
        # Create a new session for each test
        self.session = Session()

    def tearDown(self):
        # Rollback the session and close after each test
        self.session.rollback()
        self.session.close()

    def test_borrow_book_valid(self):
        # Test borrowing a valid book that is available
        book = Book(id="12345678901261", title="Available Book", author="Author", year=2022, available=True)
        self.session.add(book)
        self.session.commit()
        borrowed_book = self.session.query(Book).filter_by(id="12345678901261").first()
        borrowed_book.available = False
        self.session.commit()

        # Verify the book is marked as borrowed
        updated_book = self.session.query(Book).filter_by(id="12345678901261").first()
        self.assertFalse(updated_book.available)
        self.assertEqual(updated_book.title, "Available Book")

    def test_borrow_book_not_found(self):
        # Test borrowing a book that doesn't exist
        non_existent_book = self.session.query(Book).filter_by(id="9999999999999").first()
        self.assertIsNone(non_existent_book)

    def test_borrow_book_not_available(self):
        # Test borrowing a book that is already borrowed
        book = Book(id="12345678901241", title="Already Borrowed Book", author="Author", year=2022, available=False)
        self.session.add(book)
        self.session.commit()

        # Try to borrow the book again
        borrowed_book = self.session.query(Book).filter_by(id="1234567890124").first()
        self.assertFalse(borrowed_book.available)

if __name__ == "__main__":
    unittest.main()
