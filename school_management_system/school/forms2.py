from django.contrib.auth import password_validation
from django.forms import fields
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.forms.widgets import DateInput
from django_countries.fields import CountryField

class FeeReceiptForm(forms.ModelForm):
    class Meta:
        model=FeeReceipt
        fields=['full_name','stage','exams','co_ocurricular_activities','hostel_charges',
        'library_charges','internet_charges','electricity_charges','food_charges','furniture_charges',
        'water_charges']
        widgets={'stage': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Search By Stage'})}