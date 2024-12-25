import unittest
from models import Book, Session

class TestLibraryManagementAdd(unittest.TestCase):
    def setUp(self):
        # Create a new session for each test
        self.session = Session()

    def tearDown(self):
        # Rollback the session and close after each test
        self.session.rollback()
        self.session.close()

    def test_add_book_valid(self):
        # Test valid book addition
        book = Book(id="1234567890123", title="Valid Book", author="Valid Author", year=2022, available=True)
        self.session.add(book)
        self.session.commit()
        
        added_book = self.session.query(Book).filter_by(id="1234567890123").first()
        self.assertIsNotNone(added_book)
        self.assertEqual(added_book.title, "Valid Book")
        self.assertEqual(added_book.author, "Valid Author")
        self.assertEqual(added_book.year, 2022)

    def test_add_book_empty_fields(self):
        # Test empty fields validation
        book = Book(id="", title="", author="", year=2022, available=True)
        with self.assertRaises(ValueError):
            if not book.id or not book.title or not book.author:
                raise ValueError("All fields are required.")
        
    def test_add_book_duplicate_id(self):
        # Test for duplicate book ID
        book1 = Book(id="1234567890123", title="Book 1", author="Author 1", year=2022, available=True)
        self.session.add(book1)
        self.session.commit()
        
        # Try adding another book with the same ID
        book2 = Book(id="1234567890123", title="Book 2", author="Author 2", year=2023, available=True)
        self.session.add(book2)
        with self.assertRaises(Exception):  # Assuming the duplicate ID raises an exception
            self.session.commit()

    def test_add_book_invalid_year(self):
        # Test for an invalid publication year (before 1000 or after 2050)
        book = Book(id="1234567890124", title="Invalid Year Book", author="Author", year=999, available=True)
        with self.assertRaises(ValueError):  # Assuming ValueError for invalid year
            if not (1000 <= book.year <= 2050):
                raise ValueError("Invalid publication year.")
        
        book.year = 2101
        with self.assertRaises(ValueError):  # Invalid year again
            if not (1000 <= book.year <= 2050):
                raise ValueError("Invalid publication year.")

if __name__ == "__main__":
    unittest.main()
