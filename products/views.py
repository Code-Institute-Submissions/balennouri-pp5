from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    View to return all the products, including sorting on the page
    and searching.
    """
    products = Product.objects.all()
    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)
