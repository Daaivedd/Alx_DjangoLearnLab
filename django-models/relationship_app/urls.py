from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [ 
    path ('books/', list_books),
    path ('', LibraryDetailView.as_view() )
]
