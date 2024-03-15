from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Wishlist
from .forms import ProductForm


def all_products(request):
    """
    View to return all the products, including sorting on the page
    and searching.

    Retrieves all products from the database and performs sorting and
    filtering based on user input.
    Sorting can be done by product name, category, or in ascending/descending
    order. Filtering can be done by category and search query.
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    curr_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search": query,
        "current_categories": categories,
        "curr_sorting": curr_sorting,
    }

    return render(request, "products/products.html", context)


def product_view(request, product_id):
    """
    View to return the product page for each one of the products
    - If the product exists, renders the product view page with details about
    the product
    - If the product does not exist, returns a 404 error page

    If the user is authenticated, checks if the product is in the user's
    wishlist and sets a flag accordingly. Passes the product and wishlist flag
    to the template context.
    """
    product = get_object_or_404(Product, pk=product_id)
    in_wishlist = False

    if request.user.is_authenticated:
        try:
            wishlist = Wishlist.objects.get(user_wishlist=request.user)
            if product in wishlist.products.all():
                in_wishlist = True
        except Wishlist.DoesNotExist:
            pass

    context = {
        "product": product,
        "in_wishlist": in_wishlist,
    }

    return render(request, "products/product_view.html", context)


@login_required
def add_product(request):
    """
    Add a product to the store thorug the product management
    - request: HttpRequest object containing metadata about the request
    - If the request method is POST and the form is valid, redirects to the
    product view page after adding the product
    - If the request method is POST and the form is invalid, displays an error
    message and renders the add product form again
    - If the request method is GET, renders the add product form
    """
    if not request.user.is_superuser:
        messages.error(
            request, "Only admin can add products"
        )
        return redirect(reverse("home"))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_view', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_product(request, product_id):
    """
    Update a product in the store page
    - request: HttpRequest object containing metadata about the request
    - product_id: The ID of the product to be updated
    - If the request method is POST and the form is valid, redirects to the
    product view page after updating the product
    - If the request method is POST and the form is invalid, displays an error
    message and renders the update form again
    - If the request method is GET, renders the update form with the current
    product data
    """
    if not request.user.is_superuser:
        messages.error(
            request, "Only admin can update products"
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_view', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/update_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store page.
    - request: HttpRequest object containing metadata about the request
    - product_id: The ID of the product to be deleted
    - Redirects to the store page after deleting the product
    """
    if not request.user.is_superuser:
        messages.error(
            request, "Only admin can delete products"
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
