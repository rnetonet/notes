import weasyprint
from cart.cart import Cart
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from . import tasks
from .forms import OrderCreateForm
from .models import Order, OrderItem


# Create your views here.
def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm(request.POST or None)

    if request.method == "POST":
        if not cart:
            messages.warning(request, "Your cart is empty. You cant place an order.")
            return render(
                request, "orders/order/create.html", {"cart": cart, "form": form}
            )

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
            
            tasks.order_created.delay(order.id)
            tasks.order_placed.delay(order.id)

            return render(request, "orders/order/created.html", {"order": order})

    return render(request, "orders/order/create.html", {"cart": cart, "form": form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/order/detail.html", {"order": order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string("orders/order/pdf.html", {"order": order})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=invoice_{order.id}.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response
