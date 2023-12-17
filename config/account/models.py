from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=16)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    occupation = models.CharField(max_length=32)

    def __str__(self):
        return self.username

