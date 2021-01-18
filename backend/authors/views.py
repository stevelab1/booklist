from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Author
from .serializers import AuthorSerializer


class AuthorListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = None

class AuthorView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class FeaturedView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Author.objects.filter(featured=True)
    serializer_class = AuthorSerializer
    pagination_class = None
