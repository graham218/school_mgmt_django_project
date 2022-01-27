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
        widgets={'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        'stage': forms.Select(attrs={'class': 'form-control'}),'exams': forms.NumberInput(attrs={'class': 'form-control'}),
        'co_ocurricular_activities': forms.NumberInput(attrs={'class': 'form-control'}),
        'hostel_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'hostel_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'hostel_charges': forms.NumberInput(attrs={'class': 'form-control'}),}