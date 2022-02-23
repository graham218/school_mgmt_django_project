from django.shortcuts import render

from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPassword
from django.views.decorators.csrf import csrf_exempt
from .models import *
from school.models import *
from school_management_system.utils import accountNumberToPk
from django.contrib import messages


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
    if request.method == 'POST':
        account_no = request.POST['admission_no']
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
                "CallBackURL": "https://4e28-41-89-192-24.ngrok.io/api/v1/c2b/callback/",
                "AccountReference": account_no,
                "TransactionDesc": "Pay School Fee"
            }
            response = requests.post(api_url, json=request, headers=headers)
            print(response.json())
            messages.success(
                request, "Fee Payment made, waiting for confirmation from the callback url")
            return redirect('/')
        else:
            messages.error(request, "Invalid phone number, please try again with a valid phone number")
            return redirect("/")
    return render(request, 'fee_payment.html', context)


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
    acc = mpesa_payment['BillRefNumber']
    # paying_fee = get_object_or_404(fee_payment, id=accountNumberToPk(acc))
    # paying_fee.user=request.user
    # paying_fee.full_name=request.user.firstname+' '+request.user.LastName
    # paying_fee.amount_paid=mpesa_payment['TransAmount']
    # paying_fee.payment_method="Mpesa"
    # paying_fee.paid=True
    # paying_fee.phone_number=mpesa_payment['MSISDN']
    # paying_fee.save()
    # updating the fee balance
    # students=get_object_or_404(Students, id=accountNumberToPk(acc))
    # students.total_fees_billed+=mpesa_payment['TransAmount']
    # stuents.total_fees_paid+=mpesa_payment['TransAmount']
    # students.balance-=mpesa_payment['TransAmount']


@csrf_exempt
@loginRequired
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
        # countdown = 7
        # while countdown > 0:
        #     time.sleep(1)
        #     countdown -= 1
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
