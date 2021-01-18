from django.urls import path
from .views import AuthorListView, AuthorView, FeaturedView

urlpatterns = [
    path('', AuthorListView.as_view()),
    path('featured', FeaturedView.as_view()),
    path('<pk>', AuthorView.as_view()),
]
