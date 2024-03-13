from django.contrib import admin
from .models import Product, Category, Wishlist


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "category",
        "price",
        "rating",
    )

    ordering = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "web_name",
        "name",
    )


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        "user_wishlist",
        )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)
