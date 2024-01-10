from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField(max_length=255)
    antonation = models.CharField(max_length=200)
    author = models.CharField(max_length=50)

    class Meta:
        db_table = 'book'


