from django.shortcuts import render,get_object_or_404, redirect
from .models import Product, Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not request.user.is_authenticated:
        messages.error(request,"You must be logged in to add items to the cart.")
        return redirect('login')
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.name} has been added to your cart.")
    return redirect('product_list')

def cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            item.total = item.product.price * item.quantity  # Calculate total for each item
        total_price = sum(item.total for item in cart_items)
    else:
        cart_items = []
        total_price = 0
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def reduce_quantity(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        messages.success(request, f"Reduced quantity of {cart_item.product.name}.")
    else:
        cart_item.delete()
        messages.success(request, f"Removed {cart_item.product.name} from your cart.")

    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f"Removed {cart_item.product.name} from your cart.")
    return redirect('cart')

@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f"Increased quantity of {cart_item.product.name}.")
    return redirect('cart')
