from django.shortcuts import render

from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPassword
from django.views.decorators.csrf import csrf_exempt
from .models import *
from school.models import *


def getAccessToken(request):
    # consumer_key = '2A8EUTy82YQuir2G7umw1ufjFDzPPQA3'
    # consumer_secret = 'EcRKxxFPvyKWBGQW'
    # api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    # r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    # mpesa_access_token = json.loads(r.text)
    # validated_mpesa_access_token = mpesa_access_token['access_token']
    # return HttpResponse(validated_mpesa_access_token)
    pass


@loginRequired
def lipa_na_mpesa_online(request):
    paybill = LipanaMpesaPassword.Business_short_code
    if request.method == 'POST' and request.POST['mpesa_number']:
        booking_id = request.POST['booking_id']
        mpesa_number = request.POST['mpesa_number']
        amount = request.POST['amount']
        if len(mpesa_number) == 12 and int(mpesa_number[0:3]) == 254:
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": 174379,
                "Password": LipanaMpesaPassword.decode_password,
                "Timestamp": LipanaMpesaPassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": 1,
                "PartyA": 254790613916,
                "PartyB": 174379,
                "PhoneNumber": int(mpesa_number),
                "CallBackURL": "https://4e28-41-89-192-24.ngrok.io/api/c2b/callback/",
                "AccountReference": "Ref01",
                "TransactionDesc": "Testing STK Push"
            }
            response = requests.post(api_url, json=request, headers=headers)
            print(response.json())
            return redirect('/')
        else:
            # booking = get_object_or_404(Students, user=request.user)
            return render(request, 'payment/summary.html', {'paying': paying, 'alert_message': 'invalid Phone number', })

    return redirect('payment/fee_payment')


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPassword.Business_short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://4e28-41-89-192-24.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://4e28-41-89-192-24.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)

@csrf_exempt
def call_back(request):
    json_data = request.body.decode('utf-8')
    loaded_data = json.loads(json_data)
    print(loaded_data)
    return JsonResponse(loaded_data)

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
        print("integrity error")
    # acc = mpesa_payment['BillRefNumber']
    # booking = get_object_or_404(Booking, id=accountNumberToPk(acc))
    # booking.paid = True
    # booking.save()

@csrf_exempt
@loginRequired
def simulate_payment(request):
    if request.is_ajax():
        booking = get_object_or_404(Booking, id=request.POST['booking_id'])
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {"ShortCode": "601481",
                   "CommandID": "CustomerPayBillOnline",
                   "Amount": booking.amount,
                   "Msisdn": 254708374149,
                   "BillRefNumber": booking.account_number()
                   }

        requests.post(api_url, json=request, headers=headers)
        # countdown = 7
        # while countdown > 0:
        #     time.sleep(1)
        #     countdown -= 1
        if booking.paid is True:
            return JsonResponse({'message': 'Payment was successful', 'code': 0})
        return JsonResponse({'message': 'We could not verify your payment', 'code': 1})

    raise Http404('Page not found')