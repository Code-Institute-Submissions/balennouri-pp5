from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    # Initialize variables
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    # Loop through bag items
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            # For items without sizes
            product = get_object_or_404(Product, pk=item_id)
            # Check if the product has a sales price
            if product.sales_price:
                total += item_data * product.sales_price
            else:
                total += item_data * product.price
            product_count += item_data
            bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                }
            )
        else:
            # For items with sizes
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data["items_by_size"].items():
                # Check if the product has a sales price
                if product.sales_price:
                    total += quantity * product.sales_price
                else:
                    total += quantity * product.price
                product_count += quantity
                bag_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "size": size,
                    }
                )

    # Calculate delivery cost
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Calculate grand total
    grand_total = delivery + total

    # Create context dictionary
    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    # Return context
    return context
