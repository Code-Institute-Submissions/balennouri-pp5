from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    View that renders the bag/cart content page
    """
    return render(request, "bag/bag.html")


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if "product_size" in request.POST:
            size = request.POST["product_size"]
        bag = request.session.get("bag", {})

        if size:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} \
                {product.name} from your shopping cart')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your \
                shopping cart')

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the products of the products the user have
    chosen
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
            messages.success(request, f'Updated size {size.upper()} \
                {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} \
                {product.name} from your shopping cart')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to \
                {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} \
                from your shopping cart')

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def add_to_bag(request, item_id):
    """
    Add product to the cart, The quantity the user choice.
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]["items_by_size"].keys():
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to \
                        {bag[item_id]["items_by_size"][size]}',
                )
            else:
                bag[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request, f"Added size {size.upper()} {product.name} \
                        to your shopping cart")
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}
            messages.success
            (request, f"Added size {size.upper()} {product.name} \
                to your shopping cart")
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f"Updated {product.name} quantity to {bag[item_id]}"
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f"Added {product.name} \
                to your shopping cart")

    request.session["bag"] = bag
    return redirect(redirect_url)
