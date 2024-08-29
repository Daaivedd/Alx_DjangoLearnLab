from django.shortcuts import render
from django.views.generic.detail import DetailView 
from django.views.generic import ListView
from .models import Book
from .models import Library

# Create your views here.
def list_books (request, *args, **kwargs):
     books = Book.objects.all()
     context = {'books': books}
     return render (request, "relationship_app/list_books.html", context)

class LibraryDetailView (ListView):
    queryset = Library.objects.all()
    template_name = "relationship_app/library_detail.html"
