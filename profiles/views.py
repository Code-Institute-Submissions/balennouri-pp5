from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from products.models import Wishlist, Product, Review
from .forms import UserProfileForm
from checkout.models import Order


def view_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    template = 'profiles/reviews.html'
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if not rating or not rating.isdigit() or not (0 <= int(rating) <= 5):
            messages.error(
                request,
                'Invalid rating. Please provide a rating between 0 and 5.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        review = Review.objects.create(
            product=product,
            user=request.user,
            rating=int(rating),
            comment=comment,
        )

        messages.success(request, 'Review added successfully!')
    else:
        messages.error(request, 'Invalid request. Please try again.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def wishlist(request):
    try:
        user_wishlist = Wishlist.objects.get(user_wishlist=request.user)
    except Wishlist.DoesNotExist:
        user_wishlist = None

    template = 'profiles/user_wish_list.html'
    context = {
        "wishlist": user_wishlist
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    wishlist, created = Wishlist.objects.get_or_create(
        user_wishlist=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f'Removed {product.name} from your wishlist.')
    else:
        wishlist.products.add(product)
        messages.success(request, f'Added {product.name} to your wishlist.')

    template = 'products/product_view.html'
    context = {
        'product': product,
        'in_wishlist': product in wishlist.products.all(),
    }

    return render(request, template, context)


@login_required
def profile(request):
    """
    * Display the user's profile

    * Retrieves the user's profile from the UserProfile model
    using get_object_or_404.

    * For POST requests, it initializes the UserProfileForm with the
    provided POST data and the user's profile instance.

    * Retrieves all orders associated with the user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile is updated!')
        else:
            messages.error(
                request, "Update failed. Please ensure the form is vaid!")
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    * Retrieve the order with the given order_number or
    return a 404 page if not found

    * Display an informational message using Django's messages framework
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
