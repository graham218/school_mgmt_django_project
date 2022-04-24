from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPassword
from django.views.decorators.csrf import csrf_exempt
from .models import *
from school.models import *
from school_management_system.utils import accountNumberToPk
from django.contrib import messages
from .forms import MpesaForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView


def getAccessToken(request):
    consumer_key = '2A8EUTy82YQuir2G7umw1ufjFDzPPQA3'
    consumer_secret = 'EcRKxxFPvyKWBGQW'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)
    pass


@login_required
def lipa_na_mpesa_online(request):
    paybill = LipanaMpesaPassword.Business_short_code
    form=MpesaForm(request.POST or None)
    if request.method == 'POST':
        account_no = request.user
        mpesa_number = request.POST['mpesa_number']
        amount = request.POST['amount']
        if len(mpesa_number) == 12 and int(mpesa_number[0:3]) == 254:
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
                "Password": LipanaMpesaPassword.decode_password,
                "Timestamp": LipanaMpesaPassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": int(amount),
                "PartyA": mpesa_number,
                "PartyB": LipanaMpesaPassword.Business_short_code,
                "PhoneNumber": mpesa_number,
                "CallBackURL": "https://django-school-mis-lte.herokuapp.com/api/v1/c2b/call_back/",
                "AccountReference": str(account_no),
                "TransactionDesc": "Pay School Fee"
            }
            response = requests.post(api_url, json=request, headers=headers)
            # messages.success(
            #     request, "Fee Payment made, waiting for confirmation from the callback url")
            return redirect('/api/v1/c2b/lipa_na_mpesa_online')
        else:
            messages.error(request, "Invalid phone number, please try again with a valid phone number")
            return redirect("/api/v1/c2b/lipa_na_mpesa_online")
    context={
        "form":form
    }
    return render(request, 'fee_payment.html', context)


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPassword.Business_short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://django-school-mis-lte.herokuapp.com/api/v1/c2b/call_back",
               "ValidationURL": "https://django-school-mis-lte.herokuapp.com/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)
# "ValidationURL": "https://django-school-mis-lte.herokuapp.com/api/v1/c2b/validation",

@csrf_exempt
def call_back(request):
    url="https://django-school-mis-lte.herokuapp.com/api/v1/c2b/call_back/"
    json_data = requests.get(url).json()
    return HttpResponse(json_data)


@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body = request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    try:
        payment = MpesaPayment(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['LastName'],
            middle_name=mpesa_payment['MiddleName'],
            description=mpesa_payment['TransID'],
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            organization_balance=mpesa_payment['OrgAccountBalance'],
            type=mpesa_payment['TransactionType'],
        )
        payment.save()
    except IntegrityError:
        messages.error(request, "Fee payment confirmation was unable to take place")
    
    # insert fee payment into fee payment table
    paying_fee = get_object_or_404(fee_payment, user=request.user)
    paying_fee.user=request.user
    paying_fee.full_name=request.user.first_name+' '+request.user.middle_name+' '+request.user.last_name
    paying_fee.amount_paid=mpesa_payment['TransAmount']
    paying_fee.payment_method="Mpesa"
    paying_fee.paid=True
    paying_fee.phone_number=mpesa_payment['MSISDN']
    bill_reference_no=mpesa_payment['BillRefNumber']
    paying_fee.save()
    # update Fee Balance
    students=get_object_or_404(Students, user=request.user)
    students.total_fees_billed+=mpesa_payment['TransAmount']
    stuents.total_fees_paid+=mpesa_payment['TransAmount']
    students.balance-=mpesa_payment['TransAmount']
    students.save()
    context={
        'first_name':mpesa_payment['FirstName'],
        'last_name':mpesa_payment['LastName'],
        'middle_name':mpesa_payment['MiddleName'],
        'description':mpesa_payment['TransID'],
        'phone_number':mpesa_payment['MSISDN'],
        'amount':mpesa_payment['TransAmount'],
        'reference':mpesa_payment['BillRefNumber'],
        'organization_balance':mpesa_payment['OrgAccountBalance'],
        'type':mpesa_payment['TransactionType'],
    }
    return render(request, 'confirmation.html', context)


@csrf_exempt
@login_required
def simulate_payment(request):
    if request.is_ajax():
        paying_fee = get_object_or_404(fee_payment, id=request.POST['fee_payment_id'])
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {"ShortCode": "601481",
                   "CommandID": "CustomerPayBillOnline",
                   "Amount": paying_fee.amount_paid,
                   "Msisdn": paying_fee.phone_number,
                   "BillRefNumber": paying_fee.bill_reference_no
                   }
        requests.post(api_url, json=request, headers=headers)
        if fee_payment.paid is True:
            return JsonResponse({'message': 'Payment was successful', 'code': 0})
        return JsonResponse({'message': 'We could not verify your payment', 'code': 1})

    raise Http404('Page not found')


@csrf_exempt
def result_view(request):
    mpesa_body = request.body.decode('utf-8')
    print(mpesa_body)
    return HttpResponse(mpesa_body)


@csrf_exempt
def timeout_view(request):
    mpesa_body = request.body.decode('utf-8')
    return HttpResponse(mpesa_body)


# class Paystack(APIView):

#     def get(self, request, reference_id):
#         url = f"https://api.paystack.co/transaction/verify/{reference_id}"
#         payload = {}
#         files = {}
#         headers = {
#             'Authorization': 'Bearer SECRET_KEY',
#             'Content-Type': 'application/json'
#         }

#         response = requests.request("GET", url, headers=headers, data= payload, files=files)
#         return Response(response)