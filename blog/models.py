from datetime import datetime

from django.db import models


# Create your models here.

class Data(models.Model):
    title = models.TextField()
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')


class Users(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=200)


class Categories(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategories(models.Model):

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




