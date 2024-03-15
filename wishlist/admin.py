from django.contrib import admin
from wishlist.models import wishList

# Register your models here.

class wishlistlineadmin(admin.ModelAdmin):
    """Class for displaying wishlist lines in admin panel"""
    list_display = (
        'user',
        'product',
    )


admin.site.register(wishList, wishlistlineadmin)