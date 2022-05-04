from django.db import models
import uuid
class User(models.Model):
    userId = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

class Product(models.Model):
    productId = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    productCategory = models.CharField(max_length=50,default='')
    productName = models.CharField(max_length=50)
    productURL = models.URLField(max_length=200)
    productPrice = models.FloatField()
    productDiscount = models.FloatField()
    productDescription = models.TextField()


def __unicode__(self):
    return self.name