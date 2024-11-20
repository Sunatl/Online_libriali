from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.ManyToManyField(Genre, related_name="books")
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to="book_covers/", null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not isinstance(self.is_available, bool):
            raise ValueError("The is_available field must be a boolean.")
        super().save(*args, **kwargs)


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrows")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrows")
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    def save(self, *args, **kwargs):
        if not isinstance(self.is_returned, bool):
            raise ValueError("The is_returned field must be a boolean.")
        super().save(*args, **kwargs)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=1)  # аз 1 то 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.rating}/5)"

    def save(self, *args, **kwargs):
        if self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        super().save(*args, **kwargs)
