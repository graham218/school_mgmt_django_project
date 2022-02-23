from django.shortcuts import get_object_or_404
from .models import *
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        payment = get_object_or_404(fee_payment, id=ipn.invoice)
        payment.paid=True
        payment.save()