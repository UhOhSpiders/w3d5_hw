from models.book import *
from datetime import date

book_1 = Book("Neuromancer", "William Gibson", "Sci-fi", False, "")
book_2 = Book("Mort", "Terry Pratchett", "Fantasy", False, "")
book_3 = Book("Lanark", "Alasdair Gray", "Fantasy", False, "")
books = [book_1, book_2, book_3]

def add_new_book(book):
    books.append(book)

def delete_book(book):
    books.pop(book)

def check_out(book):
    books[book].checked_out_status = True
    today = date.today()
    books[book].checked_out_date = today.strftime("%b-%d-%Y")

def return_book(book):
    books[book].checked_out_status = False