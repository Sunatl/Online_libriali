from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import *
from .serialayzer import *
from .filter import *

# Муаллифон
class AuthorListCreateView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name', 'birth_date']


class AuthorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Жанрҳо
class GenreListCreateView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class GenreRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Китобҳо
class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'publication_date', 'price']


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Қарзгирӣ
class BorrowListCreateView(ListCreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields =  ['borrow_date', 'return_date']
    search_fields = ['user__username', 'book__title']
    ordering_fields = ['borrow_date', 'return_date']


class BorrowRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


# Тафсирҳо
class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['rating', 'created_at']
    search_fields = ['user__username', 'book__title']
    ordering_fields = ['rating', 'created_at']


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
