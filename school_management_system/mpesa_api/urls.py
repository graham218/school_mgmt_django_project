from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
app_name='mpesa_api'

router = DefaultRouter()
# router.register('paystack', Paystack, basename='paystack')

urlpatterns = [
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

    # register, confirmation, validation and callback urls
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/lipa_na_mpesa_online', views.lipa_na_mpesa_online, name="lipa_na_mpesa_online"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/call_back', views.call_back, name="call_back"),

    # simulate
    path('c2b/simulate', views.simulate_payment, name="simulate"),

    # response
    path('c2b/callback_response', views.ConfirmResponse.as_view(), name="callback_response"),
]