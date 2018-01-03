from django.conf import settings
from django.shortcuts import get_object_or_404
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED

from orders.models import Order

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import weasyprint
from io import BytesIO


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:

        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            # Not a valid payment
            return

        # payment was successful
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        # mark the order as paid
        order.paid = True
        order.save()

        subject = 'My Shop - Invoice no. {}'.format(order.id)
        message = 'Please, find attached the invoice for your recent purchase.'
        email = EmailMessage(subject ,
                             message ,
                             'admin@myshop.com' ,
                             [order.email])
        # generate PDF
        html = render_to_string('order/pdf.html' , {'order': order})
        out = BytesIO()

        stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
        weasyprint.HTML(string=html).write_pdf(out ,
                                               stylesheets=stylesheets)
        # attach PDF file
        email.attach('order_{}.pdf'.format(order.id) ,
                     out.getvalue() ,
                     'application/pdf')
        # send e-mail
        email.send()


valid_ipn_received.connect(payment_notification)
