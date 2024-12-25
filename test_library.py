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

    def test_add_book(self):
        # Create a new book instance
        book = Book(id="12345", title="Test Book", author="Author Name", year=2024, available=True)

        # Add the book to the session
        self.session.add(book)
        self.session.commit()

        # Query the book and verify it was added
        added_book = self.session.query(Book).filter_by(id="12345").first()
        self.assertIsNotNone(added_book)
        self.assertEqual(added_book.title, "Test Book")
        self.assertEqual(added_book.author, "Author Name")
        self.assertEqual(added_book.year, 2024)
        self.assertTrue(added_book.available)

if __name__ == "__main__":
    unittest.main()
