from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

class Product(models.Model):
    productName = models.CharField(max_length=50)
    productURL = models.URLField(max_length=200)
    productPrice = models.FloatField()
    productDiscount = models.FloatField()
    productDescription = models.TextField()


def __unicode__(self):
    return self.name