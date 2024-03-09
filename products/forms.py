from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Show all fields from product model,
    so the staff can add products
    """
    class Meta:
        model = Product
        fields = '__all__'
