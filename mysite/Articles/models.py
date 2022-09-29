from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

class Commet(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    commet = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.commet
    
    def get_absolute_url(self):
        return reverse('article_list')