from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    