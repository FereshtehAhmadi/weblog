from django.db import models


class Person(models.Model):
    userName = models.CharField(max_length=30)
    firstName = models.TextField(max_length=10)
    lastName = models.TextField(max_length=15)
    password = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.userName
