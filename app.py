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

# Display the add book form
add_book()