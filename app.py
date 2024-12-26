import streamlit as st
from models import Book, Session

# Initialize database session
session = Session()

def add_book():
    st.subheader("Add New Book")
    
    # Input fields for book details with constraints
    book_id = st.text_input("Book ID (ISBN)", max_chars=13)  # Assuming ISBN length of 13 characters
    title = st.text_input("Book Title", max_chars=100)  # Limit title to 100 characters
    author = st.text_input("Author", max_chars=100)  # Limit author name to 100 characters
    year = st.number_input("Publication Year", min_value=1800, max_value=2024, value=2024)
    available = st.radio("Available?", options=["Yes", "No"], index=0)

    # Ensure all fields are filled
    if st.button("Add Book"):
        if not book_id or not title or not author:
            st.error("Please fill in all the required fields.")
        else:
            # Check if the book already exists
            existing_book = session.query(Book).filter_by(id=book_id).first()
            if existing_book:
                st.error("A book with this ID already exists.")
            else:
                # Submit the book to the database
                new_book = Book(id=book_id, title=title, author=author, year=year, available=(available == "Yes"))
                session.add(new_book)
                session.commit()
                st.success(f"Book '{title}' added successfully!")

def borrow_book():
    st.subheader("Borrow a Book")

    # Input field for book ID (ISBN)
    book_id = st.text_input("Enter Book ID (ISBN)")

    if st.button("Borrow Book"):
        # Check if the book exists
        book = session.query(Book).filter_by(id=book_id).first()

        if not book:
            st.error("No book found with this ID.")
        elif not book.available:
            st.error("This book is currently not available for borrowing.")
        else:
            # Mark the book as borrowed (update availability)
            book.available = False
            session.commit()
            st.success(f"You've successfully borrowed '{book.title}' by {book.author}!")

def return_book():
    st.subheader("Return a Book")

    # Input field for book ID (ISBN)
    book_id = st.text_input("Enter Book ID (ISBN)")

    if st.button("Return Book"):
        # Check if the book exists
        book = session.query(Book).filter_by(id=book_id).first()

        if not book:
            st.error("No book found with this ID.")
        elif book.available:
            st.error("This book is already available.")
        else:
            # Mark the book as returned (update availability)
            book.available = True
            session.commit()
            st.success(f"Thank you! You've successfully returned '{book.title}' by {book.author}.")

def view_available_books():
    st.subheader("Available Books")

    # Fetch available books from the database
    available_books = session.query(Book).filter_by(available=True).all()

    if available_books:
        # Display available books with labels
        for book in available_books:
            st.write(f"**Title**: {book.title}")
            st.write(f"**ISBN (Book ID)**: {book.id}")
            st.write(f"**Author**: {book.author}")
            st.write(f"**Publication Year**: {book.year}")
            st.write("---")
    else:
        st.write("No books are currently available.")

# Sidebar for navigation
st.sidebar.title("Library Management System")
sidebar_option = st.sidebar.radio("Select an option", ["Add Book", "Borrow Book", "Return Book", "View Available Books"])

# Display the selected functionality
if sidebar_option == "Add Book":
    add_book()
elif sidebar_option == "Borrow Book":
    borrow_book()
elif sidebar_option == "Return Book":
    return_book()
elif sidebar_option == "View Available Books":
    view_available_books()