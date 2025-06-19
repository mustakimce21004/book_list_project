from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    author_image = models.CharField(max_length=100, blank=True)  # store image filename, e.g. 'author1.jpg'

    def __str__(self):
        return self.title
