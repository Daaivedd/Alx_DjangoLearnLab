from django.urls import path
from .views import list_of_books, library_of_detail

urlpatterns = [ 
    path ('books/', list_of_books)
    path ('', library_of_detail.as_view() )
]
