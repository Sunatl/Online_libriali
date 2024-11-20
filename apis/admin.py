from django.contrib import admin
from .models import Author, Genre, Book, Borrow, Review


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "birth_date", "death_date")
    search_fields = ("name",)
    list_filter = ("birth_date", "death_date")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "publication_date", "is_available")
    search_fields = ("title", "author__name")
    list_filter = ("is_available", "publication_date")
    filter_horizontal = ("genre",)


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book", "borrow_date", "return_date", "is_returned")
    search_fields = ("user__username", "book__title")
    list_filter = ("borrow_date", "is_returned")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book", "rating", "created_at")
    search_fields = ("user__username", "book__title")
    list_filter = ("rating", "created_at")
