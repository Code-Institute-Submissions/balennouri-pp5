from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Wishlist
from .forms import ProductForm


class AllProductsView(ListView):
    """
    View class for displaying all products.

    This class-based view displays a list of all products.
    It allows filtering and sorting
    of products based on various criteria such as
    search query, category, and sorting options.
    """
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        """
        Return the queryset of products based on filter and sorting options.
        """
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        sort_key = self.request.GET.get('sort')
        direction = self.request.GET.get('direction')
        category = self.request.GET.get('category')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query))
        if sort_key:
            if sort_key == 'name':
                sort_key = 'lower_name'
                queryset = queryset.annotate(lower_name=Lower('name'))
            if direction == 'desc':
                sort_key = f'-{sort_key}'
            queryset = queryset.order_by(sort_key)
        if category:
            queryset = queryset.filter(category__name__in=category.split(','))

        return queryset

    def get_context_data(self, **kwargs):
        """
        Return the context data for rendering the view.
        """
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        current_categories = self.request.GET.get('category', '').split(',')
        context['current_categories'] = Category.objects.filter(
            name__in=current_categories)
        sort_key = self.request.GET.get('sort')
        direction = self.request.GET.get('direction')
        curr_sorting = f"{sort_key}_{direction}"
        context['curr_sorting'] = curr_sorting
        return context


class ProductDetailView(DetailView):
    """
    View class for displaying product details.

    This class-based view displays the details of a specific product.
    """
    model = Product
    template_name = 'products/product_view.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        """
        Return the context data for rendering the view.
        """
        context = super().get_context_data(**kwargs)
        context['in_wishlist'] = False
        if self.request.user.is_authenticated:
            try:
                wishlist = Wishlist.objects.get(
                    user_wishlist=self.request.user)
                context['in_wishlist'] = self.object in wishlist.products.all()
            except Wishlist.DoesNotExist:
                pass
        return context


@login_required
def add_product(request):
    """
    Add a new product.

    This function-based view allows an admin user to add a new product.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The HTTP response after adding the product.
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
    Update an existing product.

    This function-based view allows an admin user to
    update an existing product.

    Args:
        request: The HTTP request object.
        product_id: The ID of the product to be updated.

    Returns:
        HttpResponse: The HTTP response after updating the product.
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
    Delete a product.

    This view function deletes a product with the given product_id if
    the user is a superuser.
    If the user is not a superuser, an error message is displayed and the user
    is redirected to the home page.

    Args:
        request: The HTTP request.
        product_id (int): The ID of the product to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the 'products'
        page after successful deletion.
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
