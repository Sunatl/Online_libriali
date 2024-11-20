from django.urls import path
from .views import *

urlpatterns = [
    # Муаллифон
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),

    # Жанрҳо
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),

    # Китобҳо
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    # Қарзгирӣ
    path('borrows/', BorrowListCreateView.as_view(), name='borrow-list-create'),
    path('borrows/<int:pk>/', BorrowRetrieveUpdateDestroyView.as_view(), name='borrow-detail'),

    # Тафсирҳо
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),
]
