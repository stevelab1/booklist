from django.urls import path
from .views import BooksView, BookView, SearchView

urlpatterns = [
    path('', BooksView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', BookView.as_view()),
]
