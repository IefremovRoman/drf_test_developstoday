from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author = models.CharField(max_length=32)


class Comment(models.Model):
    author = models.CharField(max_length=32)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, blank=True, default=None, on_delete=models.CASCADE)
