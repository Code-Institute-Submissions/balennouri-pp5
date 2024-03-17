from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from products.models import Wishlist, Product, Review
from .forms import UserProfileForm, ReviewForm, ContactFormForm
from checkout.models import Order
from django.contrib.auth import logout


def contact_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.instance.user = (
                request.user if request.user.is_authenticated else None)
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!')
            return redirect('products')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        initial_data = {}
        if request.user.is_authenticated:
            user_profile = request.user.userprofile
            initial_data = {
                'name': request.user.get_full_name(),
                'email': request.user.email,
            }
        form = ContactFormForm(initial=initial_data)

    template = 'profiles/contact.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def add_review(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect(reverse('product_view', args=[product.id]))
    else:
        form = ReviewForm()

    template = 'profiles/add_review.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


def product_reviews(request):
    all_reviews = Review.objects.all()
    template = 'profiles/product_reviews.html'
    context = {
        'reviews': all_reviews
    }
    return render(request, template, context)


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
        messages.success(
            request, f'Removed {product.name} from your wishlist.')
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
    Display the user's profile.

    Retrieves the user's profile from the UserProfile model
    using get_object_or_404.

    For POST requests:
    - If 'delete_account' is present in the request data,
    deletes the user account.
    - Otherwise, it initializes the UserProfileForm with the provided POST
    data and the user's profile instance.

    Retrieves all orders associated with the user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        if 'delete_account' in request.POST:
            # Delete user account
            user = request.user
            logout(request)
            user.delete()
            messages.success(
                request, 'Your account has been deleted successfully.')
            return redirect('home')
        else:
            # Update profile information
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile is updated!')
            else:
                messages.error(
                    request, "Update failed. Please ensure the form is valid.")
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


@login_required
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
