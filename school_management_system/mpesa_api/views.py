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
import random

def getAccessToken(request):
    consumer_key = 'n9XAie1ssbthbRAKaRUAcgbVuXrJswr9'
    consumer_secret = '6gqg9iqSsgb1STWC'
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
                "CallBackURL": "https://6bc3-105-160-68-169.ngrok.io/api/v1/c2b/callback_response",
                "AccountReference": str(account_no),
                "TransactionDesc": "Pay School Fee"
            }
            response = requests.post(api_url, json=request, headers=headers)

            # insert fee payment into fee payment table
            bill_ref = random.random()
            paying_fee = fee_payment(
                user=request.user,
                full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name),
                amount_paid=amount,
                payment_method="Mpesa",
                paid=True,
                phone_number=mpesa_number,
                bill_reference_no=bill_ref
            )
            paying_fee.save()
            # update Fee Balance
            students=get_object_or_404(Students, user=request.user)
            students.total_fees_billed+=int(mpesa_payment['TransAmount'])
            students.total_fees_paid+=int(mpesa_payment['TransAmount'])
            students.balance-=int(mpesa_payment['TransAmount'])
            students.save()
            return redirect('/api/v1/c2b/lipa_na_mpesa_online')
            messages.success(request, "STK push success...Payment In Progress..")
        else:
            messages.error(request, "Invalid phone number, please try again with a valid phone number")
            return redirect("/api/v1/c2b/lipa_na_mpesa_online")
    context={
        "form":form
    }
    return render(request, 'fee_payment.html', context)


@csrf_exempt
def register_urls(request):
    consumer_key = 'VSnv0qW2jhAjKNrqlFDZpZ3NxXbvpMwt'
    consumer_secret = 'QfIReIomJXgxjxc6'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    access_token = mpesa_access_token['access_token']

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPassword.Business_short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://6bc3-105-160-68-169.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://6bc3-105-160-68-169.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)
# "ValidationURL": "https://django-school-mis-lte.herokuapp.com/api/v1/c2b/validation",

@csrf_exempt
def call_back(request):
    url="https://6bc3-105-160-68-169.ngrok.io/api/v1/c2b/call_back/"
    json_data = requests.get(url).json()
    return HttpResponse(json_data)


@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))

class ConfirmResponse(APIView):
    def get(self, request):
        url = "https://6bc3-105-160-68-169.ngrok.io/api/v1/c2b/callback_response"
        payload = {}
        files = {}
        # data = requests.get(url)
        # json_data = data.json()
        headers = {
            'Authorization': 'Bearer SECRET_KEY',
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data= payload)
        # isolate the data key from the HTTP response object
        # item_list = json_data.get('data')

        # for item in item_list:
        # name = item['name']
        # age = item['age']

        # # This will create a new instance for every object in the array from JSON response
        # YourModel.objects.create(name=name, age=age)
        return JsonResponse(json_data)

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
    except IntegrityError:
        messages.error(request, "Fee payment confirmation was unable to take place")
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
    # paying_fee = get_object_or_404(fee_payment, id=request.POST['fee_payment_id'])
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": "600995",
                "CommandID": "CustomerPayBillOnline",
                "Amount": 1000,
                "Msisdn": 254790613916,
                "BillRefNumber": "testing"
                }
    requests.post(api_url, json=request, headers=headers)
    return JsonResponse(request)
    # url = "https://6286-105-160-49-178.ngrok.io/api/v1/c2b/callback_response"
    # data = requests.get(url)
    # json_data = data.json()
    # item_list = json_data.get('data')
    # return JsonResponse(json_data)

