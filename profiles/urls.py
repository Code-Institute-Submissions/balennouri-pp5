from django.urls import path
from . import views

urlpatterns = [

    # Profile
    path('', views.ProfileView.as_view(), name='profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path(
        'order_history/<order_number>',
        views.order_history, name='order_history'),

    # Wishlist
    path(
        'wishlist/add_to_wishlist/<int:id>',
        views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),

    # Reviews
    path('reviews/', views.product_reviews, name='product_reviews'),
    path('add_review/<int:id>/', views.add_review, name='add_review'),
    path(
        'update_review/<int:review_id>/',
        views.update_review, name='update_review'),
    path(
        'review/delete/<int:review_id>/',
        views.delete_review, name='delete_review'),

    # Contact
    path('contact/', views.contact_view, name='contact_view'),
]
