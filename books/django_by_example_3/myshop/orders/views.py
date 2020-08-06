from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.
def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"],
                    price=item["price"],
                )
            cart.clear()
            return render(request, "orders/order/created.html", {"order": order})

    return render(request, "orders/order/create.html", {"cart": cart, "form": form})


