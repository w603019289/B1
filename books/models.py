from django.db import models

# Create your models here.
class book(models.Model):
    Title=models.CharField(max_length=50)
    ISBN=models.CharField(max_length=50)
    AuthorID=models.CharField(max_length=50)
    Publisher=models.CharField(max_length=50)
    PublishData=models.CharField(max_length=50)
    Price=models.CharField(max_length=50)
class Author(models.Model):
    AuthorID=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Age=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
        