from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [ 
    path ('books/', list_of_books)
    path ('', library_of_detail.as_view() )
]
