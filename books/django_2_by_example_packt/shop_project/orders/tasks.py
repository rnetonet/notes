from celery import task
from django.core.mail import send_mail

from .models import Order

@task
def order_created_task(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"Hi! {order.first_name} {order.last_name}! \n Your order has {order.items.count()}, with a total of ${order.get_total_cost}"
    mail_sent = send_mail(subject, message, "dontanswer@shop.com", [order.email], fail_silently=False)
    return mail_sent
