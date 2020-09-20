from django.db import models

# Create your models here.

class ShopProduct(models.Model):
	name = models.TextField()
	price = models.IntegerField(default=1)

