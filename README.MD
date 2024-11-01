# Books Collection App

This is a Flask application to manage a collection of books. The app allows users to **add**, **view**, **edit**, and **delete** books in a database, where each book has a title, author, and rating.

## Table of Contents
- [Project Setup](#project-setup)
- [Features](#features)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Routes](#routes)


---



### Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

# Features
- View Books: Displays all books, ordered by title.

- Add a New Book: Adds a new book to the database.

- Edit Book Rating: Updates the rating of an existing book.

# File Structure
* app.py: Main application file containing the routes.

* db.py: Database configuration and models.

* templates/: Contains HTML templates for the app.

* index.html: Home page displaying all books.

* add.html: Form to add a new book.

* edit_rating.html: Form to edit a book’s rating.

# Routes
* /: Home page, displays all books.
* /add: Form to add a new book.
* /edit: Form to edit the rating of a specific book.
 
