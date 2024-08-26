from bookshelf.models import Book

first_book = Book.objects.get(pk=1) book.title, "Nineteen Eighty-Four" 

first_book.save()