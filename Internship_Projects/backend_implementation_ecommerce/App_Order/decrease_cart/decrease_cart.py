from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from App_Order.models import Order, Cart
from App_Shop.models import Product


@login_required
def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            # Call an itme from the cart
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f"{item.name} quantity was updated.")
                return redirect("App_Order:cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
            messages.info(request, f"{item.name} quantity was updated.")
            return redirect("App_Order:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart.")
            return redirect("App_Shop:home")
    else:
        messages.info(request, "You don't have any active order.")
        return redirect("App_Shop:home")
