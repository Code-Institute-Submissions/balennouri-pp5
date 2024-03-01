from django.shortcuts import render


def view_bag(request):
    """
    View that renders the bag/cart content page
    """
    return render(request, "bag/bag.html")
