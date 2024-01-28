from django.core.management.base import BaseCommand
from books.models import Book
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("fixtures/books.json", "r", encoding="utf8") as json_file:
            file_content = json_file.read()
            templates = json.loads(file_content)

        for item in templates:
            book = Book(
                name=item["fields"]["name"],
                author=item["fields"]["author"],
                pub_date=item["fields"]["pub_date"]
            )
            book.save()
