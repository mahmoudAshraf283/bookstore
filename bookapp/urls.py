from django.urls import path
from .views import book_create, book_delete, book_detail, book_edit, book_list

app_name = "bookapp"

urlpatterns = [
    path("", book_list, name="book-list"),
    path("book/create/", book_create, name="book-create"),
    path("book/<int:pk>/",book_detail, name="book-detail"),
    path("book/<int:pk>/edit/", book_edit, name="book-edit"),
    path("book/<int:pk>/delete/",book_delete, name="book-delete"),
]
