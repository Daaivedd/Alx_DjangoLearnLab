from .models import *

author_name = "elwahm"
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)


Book.objects.all()



Librarian.objects.get(Library)