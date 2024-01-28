from django.shortcuts import render
from books.models import Book
from datetime import datetime


def books_view(request):
    template = 'books/books_list.html'

    books = [{
        "name": i.name,
        "author": i.author,
        "pub_date": i.pub_date
    }for i in Book.objects.all()
    ]

    books.sort(key=lambda x: x["pub_date"], reverse=False)

    context = {"books": books, }
    return render(request, template, context)


def date_books(request, pub_date):
    template = "books/date_book.html"

    books = [{
        "name": i.name,
        "author": i.author,
    } for i in Book.object.filter(pub_date=datetime.strptime(pub_date, "%Y-%m-%d").date())
    ]

    context = {"books": books, "pub_date": pub_date, }
    return render(request, template, context)
