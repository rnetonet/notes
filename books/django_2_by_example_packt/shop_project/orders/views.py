from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

import weasyprint
from cart.cart import Cart

from .forms import OrderCreateForm
from .models import Order, OrderItem
from .tasks import order_created_task


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            order_created_task.delay(order.id)
            cart.clear()

            return render(request, "orders/order/created.html", {"order": order})
    else:
        form = OrderCreateForm()

    return render(request, "orders/order/create.html", {"form": form, "cart": cart})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/orders/order/detail.html", {"order": order})
admin_order_detail.short_description = "Order Detail"

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string("orders/order/invoice.html", {"order": order})

    response = HttpResponse(content_type="text/pdf")
    response["Content-Disposition"] = f'attachment; filename="invoice_{order.id}.pdf"'

    weasy_html = weasyprint.HTML(string=html)
    weasy_html.write_pdf(response)

    return response
admin_order_pdf.short_description = "Invoice"