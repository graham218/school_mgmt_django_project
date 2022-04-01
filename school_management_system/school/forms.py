from django.contrib.auth import password_validation
from django.forms import fields
from .models import *
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.forms.widgets import DateInput
from django_countries.fields import CountryField


class CreateAccountStudentsForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','middle_name', 'last_name',
                  'password1', 'password2', 'profile_photo', 'is_student']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                   'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})}

class CreateAccountLecturerForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','middle_name', 'last_name',
                  'password1', 'password2', 'profile_photo', 'is_lecturer']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                   'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})}

class CreateAccountAdminForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','middle_name', 'last_name',
                  'password1', 'password2', 'profile_photo', 'is_admin']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                   'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})}

class CreateAccountSupplierForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','middle_name', 'last_name',
                  'password1', 'password2', 'profile_photo','is_supplier']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                   'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})}

class CreateAccountNonStaffForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','middle_name', 'last_name',
                  'password1', 'password2', 'profile_photo','is_non_staff']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                   'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'auto-focus': True, 'class': 'form-control', 'placeholder': 'Current Password'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm Password'}))


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))


class AddStudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['admission_no', 'full_name', 'nationality',
                  'stud_gender', 'national_ID_number', 'birth_cert_no', 'phone_number',
                  'DOB', 'date_of_admission', 'date_of_graduation', 'programme',
                  'stage', 'postal_address', 'school_email', 'school_email_password',
                  'total_fees_billed', 'total_fees_paid', 'balance']
        widgets = {'admission_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Admission Number'}),
                   'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
                   'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, Kenyan, Ugandan, Somalian'}),
                   'stud_gender': forms.RadioSelect(attrs={'id': 'value'}),
                   'national_ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter National Id Number'}),
                   'birth_cert_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Birth Certificate Number'}),
                   'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
                   'stage': forms.Select(attrs={'id': 'id_stage', 'class': 'form-control'}),
                   'DOB': DateInput(attrs={'type': 'date'}),
                   'date_of_admission': DateInput(attrs={'type': 'date'}),
                   'date_of_graduation': DateInput(attrs={'type': 'date'}),
                   'programme': forms.Select(attrs={'id': 'id_programme','class': 'form-control'}),
                   'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, PO BOX 123 Busia, Kenya'}),
                   'school_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter School Email'}),
                   'school_email_password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School Email Password'}),
                   'total_fees_billed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total Fee Billed'}),
                   'total_fees_paid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total Fee Paid'}),
                   'balance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Fee Balance'})}

class AddStudentsProfileForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['admission_no', 'full_name', 'nationality',
                  'stud_gender', 'national_ID_number', 'birth_cert_no', 'phone_number',
                  'DOB', 'date_of_admission', 'programme',
                  'stage', 'postal_address']
        widgets = {'admission_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Admission Number'}),
                   'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
                   'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, Kenyan, Ugandan, Somalian'}),
                   'stud_gender': forms.RadioSelect(attrs={'id': 'value'}),
                   'national_ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter National Id Number'}),
                   'birth_cert_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Birth Certificate Number'}),
                   'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
                   'stage': forms.Select(attrs={'id': 'id_stage', 'class': 'form-control'}),
                   'DOB': DateInput(attrs={'type': 'date'}),
                   'date_of_admission': DateInput(attrs={'type': 'date'}),
                   'programme': forms.Select(attrs={'id': 'id_programme','class': 'form-control'}),
                   'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, PO BOX 123 Busia, Kenya'})}


class EditStudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['nationality', 'national_ID_number', 'birth_cert_no', 'phone_number', 'DOB',
                  'date_of_admission', 'date_of_graduation', 'stage', 'postal_address']
        widgets = {'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, Kenyan, Ugandan, Somalian'}),
                   'national_ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter National Id Number'}),
                   'birth_cert_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Birth Certificate Number'}),
                   'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
                   'DOB': DateInput(attrs={'type': 'date'}),
                   'date_of_admission': DateInput(attrs={'type': 'date'}),
                   'date_of_graduation': DateInput(attrs={'type': 'date'}),
                   'stage': forms.Select(attrs={'id': 'value', 'class': 'form-control'}),
                   'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, PO BOX 123 Busia, Kenya'})}


class AddLectureForm(forms.ModelForm):
    class Meta:
        model = Lectures
        fields = ['lec_no', 'full_name', 'nationality',
                  'lec_gender', 'national_ID_number', 'phone_number',
                  'DOB', 'postal_address', 'school_email', 'school_email_password',
                  'total_salary_billed', 'total_salary_paid', 'balance']
        widgets = {'lec_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lecture Number'}),
                   'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
                   'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, Kenyan, Ugandan, Somalian'}),
                   'lec_gender': forms.RadioSelect(attrs={'id': 'lec_gender'}),
                   'national_ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter National Id Number'}),
                   'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
                   'DOB': DateInput(attrs={'type': 'date'}),
                   'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, PO BOX 123 Busia, Kenya'}),
                   'school_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter School Email'}),
                   'school_email_password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School Email Password'}),
                   'total_salary_billed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total Salary Billed'}),
                   'total_salary_paid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total Salary Paid'}),
                   'balance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Salary Balance'})}


class AddLectureProfileForm(forms.ModelForm):
    class Meta:
        model = Lectures
        fields = ['lec_no', 'full_name', 'nationality',
                  'lec_gender', 'national_ID_number', 'phone_number',
                  'DOB', 'postal_address']
        widgets = {'lec_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lecture Number'}),
                   'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
                   'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, Kenyan, Ugandan, Somalian'}),
                   'lec_gender': forms.RadioSelect(attrs={'id': 'lec_gender'}),
                   'national_ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter National Id Number'}),
                   'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
                   'DOB': DateInput(attrs={'type': 'date'}),
                   'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, PO BOX 123 Busia, Kenya'})}

class EditLectureForm(forms.ModelForm):
    class Meta:
        model = Lectures
        fields = ['nationality', 'national_ID_number', 'phone_number',
                  'DOB', 'postal_address']
        widgets = {'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, Kenyan, Ugandan, Somalian'}),
                   'national_ID_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter National Id Number'}),
                   'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
                   'DOB': DateInput(attrs={'type': 'date'}),
                   'postal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg, PO BOX 123 Busia, Kenya'})}


class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['school']
        widgets = {'school': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'eg: School Of Computing & Informatics'})}


class AddProgrammesForm(forms.ModelForm):
    class Meta:
        model = Programmes
        fields = ['name', 'faculty']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Bachelor Of Science Information & Communication Technology'}),
                   'faculty': forms.Select(attrs={'class': 'form-control'})}


class AddStagesForm(forms.ModelForm):
    class Meta:
        model = Stages
        fields = ['year']
        widgets = {'year': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Year Of Study, eg: Year 1 Semester 2'})}


class AddGenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = ['gender']
        widgets = {'gender': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'eg: Male. Female, Other'})}


class AddUnitsForm(forms.ModelForm):
    class Meta:
        model = Units
        fields = ['unit_name']
        widgets = {'unit_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'eg: Calculus, Probability & Statistics, Descrete Structures'})}

#==============================================================================================
class UnitRegistrationForm(forms.ModelForm):
    class Meta:
        model = marks_yr1
        fields = ['stage', 'unit_or_subject_name']
        widgets = {'stage': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Choose your year of study'}),
            'unit_or_subject_name': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Select Unit or Subject to register'})}

class UnitRegistrationForm2(forms.ModelForm):
    class Meta:
        model = marks_yr2
        fields = ['stage', 'unit_or_subject_name']
        widgets = {'stage': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Choose your year of study'}),
            'unit_or_subject_name': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Select Unit or Subject to register'})}

class UnitRegistrationForm3(forms.ModelForm):
    class Meta:
        model = marks_yr3
        fields = ['stage', 'unit_or_subject_name']
        widgets = {'stage': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Choose your year of study'}),
            'unit_or_subject_name': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Select Unit or Subject to register'})}

class UnitRegistrationForm4(forms.ModelForm):
    class Meta:
        model = marks_yr4
        fields = ['stage', 'unit_or_subject_name']
        widgets = {'stage': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Choose your year of study'}),
            'unit_or_subject_name': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Select Unit or Subject to register'})}

class UnitRegistrationForm5(forms.ModelForm):
    class Meta:
        model = marks_yr5
        fields = ['stage', 'unit_or_subject_name']
        widgets = {'stage': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Choose your year of study'}),
            'unit_or_subject_name': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Select Unit or Subject to register'})}

class UnitRegistrationForm6(forms.ModelForm):
    class Meta:
        model = marks_yr6
        fields = ['stage', 'unit_or_subject_name']
        widgets = {'stage': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Choose your year of study'}),
            'unit_or_subject_name': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Select Unit or Subject to register'})}

class UnitRegistrationForm7(forms.ModelForm):
    class Meta:
        model = marks_yr7
        fields = ['stage', 'unit_or_subject_name']
        widgets = {'stage': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Choose your year of study'}),
            'unit_or_subject_name': forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'Select Unit or Subject to register'})}
#===============================================================================================
class MarksForm(forms.ModelForm):
    class Meta:
        model = marks_yr1
        fields = ['marks', 'grade']
        widgets = {'marks': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Marks'}),
            'grade': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Grade'})}

class MarksForm2(forms.ModelForm):
    class Meta:
        model = marks_yr2
        fields = ['marks', 'grade']
        widgets = {'marks': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Marks'}),
            'grade': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Grade'})}

class MarksForm3(forms.ModelForm):
    class Meta:
        model = marks_yr3
        fields = ['marks', 'grade']
        widgets = {'marks': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Marks'}),
            'grade': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Grade'})}

class MarksForm4(forms.ModelForm):
    class Meta:
        model = marks_yr4
        fields = ['marks', 'grade']
        widgets = {'marks': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Marks'}),
            'grade': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Grade'})}

class MarksForm5(forms.ModelForm):
    class Meta:
        model = marks_yr5
        fields = ['marks', 'grade']
        widgets = {'marks': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Marks'}),
            'grade': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Grade'})}

class MarksForm6(forms.ModelForm):
    class Meta:
        model = marks_yr6
        fields = ['marks', 'grade']
        widgets = {'marks': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Marks'}),
            'grade': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Grade'})}

class MarksForm7(forms.ModelForm):
    class Meta:
        model = marks_yr7
        fields = ['marks', 'grade']
        widgets = {'marks': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Marks'}),
            'grade': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Unit Grade'})}
#==========================================================================================
class PayFeesPayPalForm(forms.ModelForm):
    class Meta:
        model=fee_payment
        fields=['amount_paid']
        widgets = {'amount_paid': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Amount In US Dollars'})}
        
class SchoolFeePaymentForm(forms.ModelForm):
    class Meta:
        model=fee_payment
        fields=['user','full_name','phone_number','amount_paid','payment_method','paid','bill_reference_no']
        widgets = {'user': forms.Select(
            attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'phone_number': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'amount_paid': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Amount In Kenyan Shillings'}),
            'payment_method': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Payment Method'}),
            'bill_reference_no': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Bill Reference Number'})}

class SalaryPaymentForm(forms.ModelForm):
    class Meta:
        model=salary_payment
        fields=['user','full_name','phone_number','amount_paid','payment_method','paid','bill_reference_no']
        widgets = {'user': forms.Select(
            attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'phone_number': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'amount_paid': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Amount In Kenyan Shillings'}),
            'payment_method': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Payment Method'}),
            'bill_reference_no': forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Bill Reference Number'})}