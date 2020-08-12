from io import BytesIO
from celery import task
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
import weasyprint

from .models import Order


@task
def order_created(order_id):
    """
    Send e-mail to customer asynchronously after an Order is made.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order_id}"
    body = f"""Dear {order.name}, 
    Your order {order.id} was successfully created.
    """
    mail_sent = send_mail(subject, body, "admin@myshop.com", [order.email])


@task
def order_placed(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"Your invoice for order {order.id}"
    message = "Please see the invoice attached"
    email = EmailMessage(subject, message, "admin@myshop.com", [order.email])
    html = render_to_string("orders/order/pdf.html", {"order": order})
    out = BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)
    email.attach(f"invoice_{order.id}.pdf", out.getvalue(), "application/pdf")
    email.send()
