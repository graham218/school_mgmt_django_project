from django.contrib.auth import password_validation
from django.forms import fields
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.forms.widgets import DateInput
from django_countries.fields import CountryField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FeeReceiptForm(forms.ModelForm):
    class Meta:
        model=FeeReceipt
        fields=['full_name','stage','exams','co_ocurricular_activities','hostel_charges',
        'library_charges','internet_charges','electricity_charges','food_charges','furniture_charges',
        'water_charges']
        widgets={'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        'stage': forms.Select(attrs={'class': 'form-control'}),
        'exams': forms.NumberInput(attrs={'class': 'form-control'}),
        'co_ocurricular_activities': forms.NumberInput(attrs={'class': 'form-control'}),
        'hostel_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'library_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'internet_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'electricity_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'food_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'furniture_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'water_charges': forms.NumberInput(attrs={'class': 'form-control'})}

class SpecialExamRegisterForm(forms.ModelForm):
    class Meta:
        model=SpecialExam
        fields=['stage','unit_name']
        widgets={'stage': forms.Select(attrs={'class': 'form-control'}),
        'unit_name': forms.Select(attrs={'class': 'form-control'})}

class SpecialExamMarksForm(forms.ModelForm):
    class Meta:
        model=SpecialExam
        fields=['marks','grade', 'comments']
        widgets={'marks': forms.NumberInput(attrs={'class': 'form-control'}),
        'grade': forms.TextInput(attrs={'class': 'form-control'}),
        'comments': forms.TextInput(attrs={'class': 'form-control'})}

class LecturerUnitsForm(forms.ModelForm):
    class Meta:
        model=LecturerUnits
        fields=['unit_name','level_of_understanding']
        widgets={'stage': forms.Select(attrs={'class': 'form-control'}),
        'unit_name': forms.Select(attrs={'class': 'form-control'}),
        'level_of_understanding': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Professional, Advanced'})}

class NoticeBoardForm(forms.ModelForm):
    notice=forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model=NoticeBoard
        fields=['group','notice_title','notice','signature']
        widgets={'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        'notice_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'eg: Inviting all students to the incoming meeting'}),
        'signature': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'eg MIT'}),
        'group': forms.Select(attrs={'class': 'form-control'})}

class VotingForm(forms.ModelForm):
    class Meta:
        model=Voting
        fields=['full_name','stage','course','seat']
        widgets={'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        'stage': forms.Select(attrs={'class': 'form-control'}),
        'course': forms.Select(attrs={'class': 'form-control'}),
        'seat': forms.Select(attrs={'class': 'form-control'})}

class SuggestionBoxForm(forms.ModelForm):
    suggestion=forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model=SuggestionBox
        fields=['full_name','suggestion']
        widgets={'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        'stage': forms.Select(attrs={'class': 'form-control'}),
        'suggestion': forms.TextInput(attrs={'class': 'form-control'})
        }

class SeatsForm(forms.ModelForm):
    class Meta:
        model=Seats
        fields=['seat']
        widgets={'seat': forms.TextInput(attrs={'class': 'form-control'})}

class FeePaymentForm(forms.ModelForm):
    fee_payment_id=forms.CharField(label=_("Fee Payment ID"), widget=forms.TextInput(
        attrs={'placeholder': 'ie any random number', 'class': 'form-control'}))
    mpesa_number=forms.CharField(label=_("Fee Payment ID"), widget=forms.TextInput(
        attrs={'placeholder': 'format: 254............', 'class': 'form-control'}))
    amount=forms.DecimalField(label=_("Fee Payment ID"), widget=forms.NumberInput(
        attrs={'class': 'form-control'}))