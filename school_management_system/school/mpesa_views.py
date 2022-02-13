from django.shortcuts import render, redirect
from .forms2 import FeePaymentForm

def pay_fee(request):
    title="Pay School Fee Using Mpesa"
    button="Pay School Fee"
    form=FeePaymentForm(request.POST or None)
    context={
        "title":title,
        "form": form,
        "button":button
    }
    return render(request, "mpesa_payment/fee_payment.html",context)