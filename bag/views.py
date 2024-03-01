from django.shortcuts import render, redirect


def view_bag(request):
    """
    View that renders the bag/cart content page
    """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """
    Add product to the cart, The quantity the user choice.
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)