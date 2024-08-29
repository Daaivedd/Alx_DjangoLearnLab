from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import *
# Create your views here.
def list_of_books (request, *args, **kwargs):
     books = Book.objects.all()
     context = {'books': books}
     return render (request, "relationship_app/list_books.html", context)

class library_of_detail (ListView):
    queryset = Library.objects.all()
    template_name = "templates/library_detail.html"
