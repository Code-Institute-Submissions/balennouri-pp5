from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history, name='order_history'),
    path(
        'wishlist/add_to_wishlist/<int:id>',
        views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
]
