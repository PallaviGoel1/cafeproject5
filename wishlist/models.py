from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.

class wishList(models.Model):
    """Model for Wishlist object"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)