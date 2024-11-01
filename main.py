from flask import Flask, render_template, request, redirect, url_for
from db import db, Books



# todo: Add a Delete Anchor Tag to each book listing <li>. When clicked it should delete the book from the database and redirect back to the home page. e.g.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with the app
db.init_app(app)


@app.route('/')
def home():
    result = Books.query.order_by(Books.title).all()
    # GOING FOR RESULT FOR PERFORMANCE
    # result = db.session.execute(db.select(Books).order_by(Books.title))
    # all_books = list(result.scalars())
    # for book in all_books:
    #     print(f"Title: {book.title}, Author: {book.author}")
    return render_template("index.html", books=result)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE
        with app.app_context():
            new_book = Books(title=request.form["title"], author=request.form["author"],
                             rating=int(request.form["rating"]))
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Books, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Books, book_id)
    return render_template("edit_rating.html", book=book_selected)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

