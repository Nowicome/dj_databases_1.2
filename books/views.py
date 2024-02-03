from django.shortcuts import render
from books.models import Book


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

    books_objects = Book.objects.filter(pub_date=pub_date)
    prev_book = Book.objects.filter(pub_date__lt=pub_date).order_by("-pub_date").first()
    next_book = Book.objects.filter(pub_date__gt=pub_date).order_by("pub_date").first()

    if prev_book:
        prev_book = str(prev_book.pub_date)
    if next_book:
        next_book = str(next_book.pub_date)

    context = {"books": books_objects, "prev_book": prev_book, "next_book": next_book, }
    return render(request, template, context)
