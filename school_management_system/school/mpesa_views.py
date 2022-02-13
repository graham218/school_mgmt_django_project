from django.shortcuts import render, redirect

def pay_fee(request):
    title="Pay School Fee Using Mpesa"
    button="Pay School Fee"
    context={
        "title":title,
        "button":button
    }
    return render(request, "mpesa_payment/fee_payment.html",context)