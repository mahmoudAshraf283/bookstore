from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, ISBN

@receiver(post_save, sender=Book)
def create_isbn_for_book(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'isbn'):
        ISBN.objects.create(
            book=instance,
            author_name=instance.user.username if instance.user else "Anonymous",
            book_title=instance.title
        )
