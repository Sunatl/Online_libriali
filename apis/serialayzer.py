from rest_framework import serializers
from .models import Author, Genre, Book, Borrow, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "biography", "birth_date", "death_date"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "author",
            "genre",
            "publication_date",
            "cover_image",
            "is_available",
            "created_at",
            "updated_at",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = {
            "id": instance.author.id,
            "name": instance.author.name,
        }
        representation["genre"] = [
            {"id": genre.id, "name": genre.name} for genre in instance.genre.all()
        ]
        return representation


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = [
            "id",
            "user",
            "book",
            "borrow_date",
            "return_date",
            "is_returned",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = {
            "id": instance.user.id,
            "username": instance.user.username,
        }
        representation["book"] = {
            "id": instance.book.id,
            "title": instance.book.title,
        }
        return representation


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "book",
            "review_text",
            "rating",
            "created_at",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user"] = {
            "id": instance.user.id,
            "username": instance.user.username,
        }
        representation["book"] = {
            "id": instance.book.id,
            "title": instance.book.title,
        }
        return representation
