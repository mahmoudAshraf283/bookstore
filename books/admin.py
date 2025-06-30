from django.contrib import admin
from .models import Book, Category, ISBN

class ISBNInline(admin.StackedInline):
    model = ISBN
    can_delete = False

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'views', 'user')
    list_filter = ('rate', 'categories')
    inlines = [ISBNInline]

admin.site.register(Category)
