# utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_order_notification(order):
    subject = f"New Order Placed by {order.user.username}"
    message = f"Order Details:\n\nProduct: {order.product.name}\nQuantity: {order.quantity}\nPrice: {order.product.price}\n\nOrder ID: {order.id}\nOrder Date: {order.order_date}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['admin@example.com']  # Add your email or admin email
    send_mail(subject, message, email_from, recipient_list)
