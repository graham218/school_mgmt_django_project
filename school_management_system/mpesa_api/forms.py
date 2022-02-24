from django import forms
from django.utils.translation import gettext, gettext_lazy as _

class MpesaForm(forms.Form):
    mpesa_number = forms.CharField(label=_("M-Pesa Number"), widget=forms.TextInput(
        attrs={'placeholder': 'eg: 254790613916', 'class': 'form-control'}))
    amount = forms.CharField(label=_("Amount To Pay"), widget=forms.TextInput(
        attrs={'class': 'form-control'}))