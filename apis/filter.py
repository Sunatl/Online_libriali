from django_filters import rest_framework as filters
from .models import *



class BookFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')  # Филтри нархи камтарин
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')  # Филтри нархи зиёдтарин

    class Meta:
        model = Book
        fields = ['title', 'author__id', 'genre__id', 'publication_date']


