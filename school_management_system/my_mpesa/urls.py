from django.urls import path, include
from . import views

app_name='my_mpesa'

urlpatterns = [
    path('', views.index, name='index'),
    # path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
]