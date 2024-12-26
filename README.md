Here’s how you can expand your README with the steps you mentioned:

```markdown
# Library Management System

This is a simple Library Management System developed in Python using Streamlit for the interface and SQL for the database.

## Features

- Add new books to the library.
- Borrow books while checking their availability.
- Return borrowed books and update their status.
- View all available books in the library.

## Requirements

- Python 3.9 or above
- Streamlit
- SQLAlchemy

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run `models.py` to create the database:
   ```bash
   python models.py
   ```

6. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Running the Testing Suite

To run the tests for the Library Management System, use the following command:

```bash
python test_add_library.py
python test_borrow_library.py
python test_available_library.py
python test_return_library.py
