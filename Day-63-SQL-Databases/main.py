from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.String(4), unique=False, nullable=False)


db.create_all()


@app.route("/")
def home():
    all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Books(title=request.form["title"],
                         author=request.form["author"],
                         rating=request.form["rating"])

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/amend/<book_id>", methods=['GET', 'POST'])
def amend(book_id):
    selected_book = db.session.query(Books).get(book_id)

    if request.method == "POST":
        selected_book.rating = request.form["new_rating"]

        db.session.commit()

        return redirect(url_for("home"))
    return render_template("amend.html", book=selected_book)


if __name__ == "__main__":
    app.run(debug=True)

