from django.db import models


class Person(models.Model):
    userName = models.CharField(max_length=30)
    firstName = models.TextField(max_length=10)
    lastName = models.TextField(max_length=15)
    password = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.userName


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    