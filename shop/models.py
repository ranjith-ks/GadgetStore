from django.db import models
import uuid
class User(models.Model):
    userId = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Product(models.Model):
    productId = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    productCategory = models.CharField(max_length=50,default='')
    productName = models.CharField(max_length=50)
    productURL = models.URLField(max_length=500)
    productPrice = models.FloatField()
    productDescription = models.TextField()

    def __str__(self):
        return self.productName


def __unicode__(self):
    return self.name