from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid

class Category(models.Model):
    name = models.CharField(max_length=50)

    def clean(self):
        if len(self.name) < 2:
            raise ValidationError("Category name must be at least 2 characters.")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField(default=0.0)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    categories = models.ManyToManyField(Category)

    def clean(self):
        if not (10 <= len(self.title) <= 50):
            raise ValidationError("Title must be between 10 and 50 characters.")

    def __str__(self):
        return self.title

class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return str(self.isbn_number)
