from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.TextField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Shop(models.Model):
    image = models.TextField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.TextField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    position = models.TextField()
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.TextField()
    name = models.CharField()
    content = models.TextField()

    def __str__(self):
        return self.name
