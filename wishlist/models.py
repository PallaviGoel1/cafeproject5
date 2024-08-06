from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.conf import settings

from products.models import Product


class wishList(models.Model):
    """Model for Wishlist object"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}"