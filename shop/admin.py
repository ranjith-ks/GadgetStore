from django.contrib import admin
from shop import models

admin.site.register(models.Customer)
admin.site.register(models.Product)