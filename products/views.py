from django.shortcuts import render, get_object_or_404
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


def product_view(request, product_id):
    """
    View to return the product page for each one og the products
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }

    return render(request, "products/product_view.html", context)

