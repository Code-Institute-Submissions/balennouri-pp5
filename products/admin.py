from django.contrib import admin
from .models import Product, Category, Wishlist, Review


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


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "rating",
        )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Review, ReviewAdmin)
