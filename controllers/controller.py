from flask import render_template, request, redirect
from app import app
from models.library import *
from models.book import *

@app.route('/')
def index():
    return render_template("index.html", book_list = books)

@app.route('/', methods=['POST'])
def add_book():
    print(request.form)
    book_name = request.form["book_name"]
    author_name = request.form["author_name"]
    genre = request.form["genre"]
    new_book = Book(book_name, author_name, genre, False, "")
    add_new_book(new_book)
    return redirect("/")

@app.route('/book/<index>')
def book(index):
    return render_template("book.html", book = books[(int(index))])

@app.route('/book/delete/<index>', methods=['POST'])
def del_book(index):
    delete_book(int(index))
    return redirect("/")

@app.route('/book/check-out/<index>', methods=['POST'])
def check_out_book(index):
    print(request.form)
    check_out(int(index))
    return redirect("/")

@app.route('/book/return-book/<index>', methods=['POST'])
def return_book_form(index):
    print(request.form)
    return_book(int(index))
    return redirect("/")

