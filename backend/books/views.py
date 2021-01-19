from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer

class BooksView(ListAPIView):
    queryset = Book.objects.order_by('-updated').filter(is_published=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = BookSerializer
    lookup_field = 'slug'

class BookView(RetrieveAPIView):
    queryset = Book.objects.order_by('-updated').filter(is_published=True)
    serializer_class = BookDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = BookSerializer

    def post(self, request, format=None):
        queryset = Book.objects.order_by('-updated').filter(is_published=True)
        data = self.request.data

        title = data['title']
        queryset = queryset.filter(title__icontains=title)

        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        section = data['section']
        queryset = queryset.filter(section__iexact=section)

        mood = data['mood']
        queryset = queryset.filter(mood__iexact=mood)
        
        featured = data['featured']
        queryset = queryset.filter(featured__iexact=featured)

        free_version_available = data['free_version_available']
        queryset = queryset.filter(free_version_available__iexact=free_version_available)

        serializer = BookSerializer(queryset, many=True)

        return Response(serializer.data)