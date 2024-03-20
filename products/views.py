from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Wishlist
from .forms import ProductForm


class AllProductsView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_queryset(self):
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
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        current_categories = self.request.GET.get('category', '').split(',')
        context['current_categories'] = Category.objects.filter(
            name__in=current_categories)
        context['curr_sorting'] = (
            f"{self.request.GET.get('sort')}_{self.request.GET.get('direction')}"
            )
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_view.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
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
    if not request.user.is_superuser:
        messages.error(
            request, "Only admin can delete products"
        )
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
