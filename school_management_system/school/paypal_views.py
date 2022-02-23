from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import *
from .forms import *

from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt


def send_payment(request):
    if request.method == 'POST':
        form = PayFeesPayPalForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            payment= fee_payment(
                user = request.user,
                full_name=request.user.first_name+' '+request.user.middle_name+' '+request.user.last_name,
                amount_paid = cleaned_data.get('amount_paid'),
                payment_method = 'PAY-PAL',
                bill_reference_no = request.user.email,
            )
            payment.save()
            request.session['payment_id'] = payment.id
            return redirect('school:process_payment')
    else:
        form = PayFeesPayPalForm()
        return render(request, 'paypal/pay_fee_paypal.html', {'form': form})

def process_payment(request):
    payment_id = request.session.get('payment_id')
    payment_f = get_object_or_404(fee_payment, id=payment_id)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(payment_f.amount_paid),
        'item_name': 'School Fee',
        'invoice': str(payment_f.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('school:payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('school:payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal/process_payment.html', {'payment_f': payment_f, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'paypal/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'paypal/payment_cancelled.html')