from .models import *

author_name = "elwahm"
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)


library = Library.objects.get(name=library_name)
Library.books.all()




Librarian.objects.get(Library=library_name )