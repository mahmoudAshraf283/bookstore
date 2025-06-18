from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255, default="")
    author = models.CharField(max_length=255, default="")
    desc = models.TextField(default="")
    rate = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
