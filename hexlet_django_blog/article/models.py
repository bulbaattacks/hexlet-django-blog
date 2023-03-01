from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=201)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
