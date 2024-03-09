from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    web_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_for_web(self):
        return self.web_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_sales = models.BooleanField(default=False)
    sales_price = models.DecimalField(
        default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name
