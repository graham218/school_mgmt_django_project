from django.contrib.auth import password_validation
from django.forms import fields
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _



#class RegistrationForm(UserCreationForm):
#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password1', 'password2']
#        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
#        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter Email Address'}),
#        'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'password1'}),
#        'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'password2'})}

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2','is_staff','is_active','is_superuser']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['locality', 'city', 'state']
        widgets = {'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Popular Place like Restaurant, Religious Site, etc.'}),
         'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
          'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State or Province'})}


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'auto-focus':True, 'class':'form-control', 'placeholder':'Current Password'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'New Password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'Confirm Password'}))


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))


class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))


class AddStudentsForm(forms.ModelForm):
    class Meta:
        model=Students
        fields=['admission_no', 'full_name', 'nationality',
     'gender', 'national_ID_number', 'birth_cert_no', 'phone_number',
     'DOB', 'date_of_admission', 'date_of_graduation', 'programme',
     'stage','profile_photo', 'postal_address', 'school_email', 'school_email_password',
     'total_fees_billed', 'total_fees_paid', 'balance']

    widgets = {'admission_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Admission Number'}),
        'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Full Name'}),
        'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'eg, Kenyan, Ugandan, Somalian'}),
        'gender': forms.RadioSelect(attrs={'id': 'value'}),
        'national_ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter National Id Number'}),
        'birth_cert_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Birth Certificate Number'}),
        'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Phone Number'}),
        'stage': forms.RadioSelect(attrs={'id': 'value'}),
        'profile_photo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Full Name'}),
        'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'eg, PO BOX 123 Busia, Kenya'}),
        'school_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter School Email'}),
        'school_email_password': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'School Email Password'})}

class AddLectureForm(forms.ModelForm):
    class Meta:
        model=Lectures
        fields=['lec_no', 'full_name', 'nationality',
     'gender', 'national_ID_number', 'phone_number',
     'DOB','postal_address', 'school_email', 'school_email_password',
     'total_salary_billed', 'total_salary_paid', 'balance']

class AddFacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields=['school']

class AddProgrammes(forms.ModelForm):
    class Meta:
        model=Programmes
        fields=['name','faculty']

class AddStages(forms.ModelForm):
    class Meta:
        model=Stages
        fields=['year']

class AddGender(forms.ModelForm):
    class Meta:
        model=Gender
        fields=['gender']

class AddUnits(forms.ModelForm):
    class Meta:
        model=Units
        fields=['unit_name']