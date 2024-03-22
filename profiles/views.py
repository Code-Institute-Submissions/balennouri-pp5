from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from products.models import Wishlist, Product, Review
from .forms import UserProfileForm, ReviewForm, ContactFormForm
from checkout.models import Order
from django.contrib.auth import logout


def contact_view(request):
    """
    Display a contact form for users to send messages.

    If the request method is POST:
    * Validate the form data.
    * If the form is valid, save the message and display a success message.
    * If the form is invalid, display error messages.

    If the request method is GET:
    * Initialize the contact form with initial data
    if the user is authenticated.
    """
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
def delete_review(request, review_id):
    """
    Allow users to delete their reviews if they are the owners.

    * Retrieve the review object based on the provided review_id.

    * Check if the current user is the owner of the review;
    if yes, delete the review.

    * Display success or error messages accordingly.
    """
    review = get_object_or_404(Review, id=review_id)

    if request.user == review.user:
        review.delete()
        messages.success(request, 'Review deleted successfully!')
    else:
        messages.error(request, "You are not allowed to delete this review.")

    return redirect(reverse('product_reviews'))


@login_required
def update_review(request, review_id):
    """
    Allow users to update their reviews if they are the owners.

    * Retrieve the review object based on the provided review_id.

    * Check if the current user is the owner of the review;
    if not, display an error message.

    * If the request method is POST, validate the form and
    update the review if valid.

    * Display success or error messages accordingly.

    * Otherwise, initialize the form with the review instance for editing.
    """
    review = get_object_or_404(Review, id=review_id)

    if request.user != review.user:
        messages.error(request, "You are not allowed to update this review.")
        return redirect(reverse('product_reviews'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect(reverse('product_reviews'))
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ReviewForm(instance=review)

    template = 'profiles/update_review.html'
    context = {
        'form': form,
        'review': review,
        'product': review.product,
    }
    return render(request, template, context)


@login_required
def add_review(request, id):
    """
    Allow logged-in users to add reviews for products.

    * Retrieves the product object based on the provided id or returns a 404
    error if not found.

    * If the request method is POST, validates the submitted form data.

    * If the form data is valid, creates a new review associated
    with the product and the logged-in user.

    * Redirects the user to the product view page after
    successfully adding the review.

    * If the request method is GET, renders the add_review
    template with an empty form.
    """
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
    """
    Render the page displaying all product reviews.

    Retrieves all reviews from the database.
    Renders the 'product_reviews.html' template with the list of reviews.
    """
    all_reviews = Review.objects.all()
    template = 'profiles/product_reviews.html'
    context = {
        'reviews': all_reviews
    }
    return render(request, template, context)


@login_required
def wishlist(request):
    """
    Retrieve the user's wishlist if it exists, otherwise, return None.

    * Retrieves the user's wishlist from the database based
    on the logged-in user.

    * If the wishlist exists, it is passed to the template context.

    * If the wishlist does not exist, None is returned and
    no wishlist is displayed.
    """
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
    """
    * Retrieve the product object or return a 404 error if not found
    * Get or create the user's wishlist
    * Check if the product is already in the wishlist
    * If the product is not in the wishlist, add it
    """
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
            user = request.user
            logout(request)
            user.delete()
            messages.success(
                request, 'Your account has been deleted successfully.')
            return redirect('home')
        else:
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
