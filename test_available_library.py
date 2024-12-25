import unittest
from models import Book, Session

class TestLibraryManagementView(unittest.TestCase):
    def setUp(self):
        # Create a new session for each test
        self.session = Session()
        self.session.query(Book).delete()
        self.session.commit()

    def tearDown(self):
        # Rollback the session and close after each test
        self.session.rollback()
        self.session.close()

    def test_no_available_books(self):
        # Ensure the database has no available books
        available_books = self.session.query(Book).filter_by(available=True).all()
        self.assertEqual(len(available_books), 0, "There should be no available books in the database.")

    def test_one_available_book(self):
        # Add one available book
        book = Book(id="1234567890123", title="Test Book", author="Test Author", year=2022, available=True)
        self.session.add(book)
        self.session.commit()

        # Fetch available books
        available_books = self.session.query(Book).filter_by(available=True).all()
        self.assertEqual(len(available_books), 1, "There should be one available book.")
        self.assertEqual(available_books[0].title, "Test Book")
        self.assertEqual(available_books[0].author, "Test Author")
        self.assertEqual(available_books[0].year, 2022)

    def test_multiple_available_books(self):
        # Add multiple available books
        book1 = Book(id="1234567890123", title="Book One", author="Author One", year=2021, available=True)
        book2 = Book(id="9876543210987", title="Book Two", author="Author Two", year=2023, available=True)
        self.session.add_all([book1, book2])
        self.session.commit()

        # Fetch available books
        available_books = self.session.query(Book).filter_by(available=True).all()
        self.assertEqual(len(available_books), 2, "There should be two available books.")
        self.assertIn("Book One", [book.title for book in available_books])
        self.assertIn("Book Two", [book.title for book in available_books])

    def test_books_after_update_availability(self):
        # Add one available book
        book = Book(id="1234567890123", title="Test Book", author="Test Author", year=2022, available=True)
        self.session.add(book)
        self.session.commit()

        # Update availability to False
        book.available = False
        self.session.commit()

        # Fetch available books
        available_books = self.session.query(Book).filter_by(available=True).all()
        self.assertEqual(len(available_books), 0, "There should be no available books after updating availability.")

if __name__ == "__main__":
    unittest.main()
