from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Admin inline class for OrderLineItem.

    This inline class allows OrderLineItem objects to be edited inline within the OrderAdmin interface.

    Attributes:
        model: The model associated with the inline.
        readonly_fields: Readonly fields displayed in the inline.
    """
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin class for Order.

    This admin class provides a custom interface for managing Order
    objects in the Django admin site.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    ordering = ("-date",)


# Register the OrderAdmin class with the Order model in the Django admin site
admin.site.register(Order, OrderAdmin)
