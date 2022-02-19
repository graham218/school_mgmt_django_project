from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
#from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(
                        request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("/accounts/password-reset/done/")
    form = PasswordResetForm()
    return render(request=request, template_name="account/password_reset.html", context={"form": form})

# Create your views here.


@login_required
def home(request):
    title = "Home"
    students_title = "Student's Dashboard"
    lecturers_title = "Lecturer's Dashboard"
    admin_title="System Administrator's Dashboard"
    supplier_title="Supplier's Dashboard"
    non_staff_title="Non-Staff Dashboard"
    students_queryset = Students.objects.filter(user=request.user)
    lec_queryset=Lectures.objects.filter(user=request.user)
    total_users=User.objects.all().count()
    # total_ghost_users=User.objects.filter(is_admin=False,is_student=False,is_lecturer=False,is_non_sfaff=False,is_supplier=False).count()
    total_students=Students.objects.all().count()
    total_lecturers=Lectures.objects.all().count()
    context = {
        "title": title,
        "students_title": students_title,
        "lecturers_title": lecturers_title,
        "admin_title": admin_title,
        "supplier_title": supplier_title,
        "non_staff_title": non_staff_title,
        "students_queryset": students_queryset,
        "lec_queryset": lec_queryset,
        "total_users": total_users,
        # "total_ghost_users": total_ghost_users,
        "total_students": total_students,
        "total_lecturers": total_lecturers,
    }
    return render(request, "index.html", context)

def all_users(request):
    queryset=User.objects.all()
    title="All Users Registered"
    context={
        "queryset":queryset,
        "title":title,
    }
    return render(request, "admin/all_users.html", context)

def all_students(request):
    queryset=Students.objects.all()
    title="All Students Registered"
    context={
        "queryset":queryset,
        "title":title,
    }
    return render(request, "admin/all_students.html", context)

def all_lecturers(request):
    queryset=Lectures.objects.all()
    title="All Lecturers Registered"
    context={
        "queryset":queryset,
        "title":title,
    }
    return render(request, "admin/all_lecturers.html", context)

def all_fee_payment(request):
    queryset=fee_payment.objects.all()
    title="All Fee Payment Records"
    context={
        "queryset":queryset,
        "title":title,
    }
    return render(request, "admin/fee_payment_records.html", context)

def all_fee_receipts(request):
    queryset=FeeReceipt.objects.all()
    title="All Fee Payment Receipts Records"
    context={
        "queryset":queryset,
        "title":title,
    }
    return render(request, "admin/fee_payment_receipts.html", context)

# Authentication Starts Here


def CreateAccountStudentsView(request):
    form = CreateAccountStudentsForm(request.POST)
    if form.is_valid():
        messages.success(
            request, "Congratulations! Registration Successful, you can now log in!")
        form.save()
    # else:
    #     messages.error(request, "An Error occured while trying to create your new account!!!")
    #     messages.success(request, "Please check if the passwords match correctly or meet the minimum requirements")
        return redirect('/accounts/login/')
    return render(request, 'account/register.html', {'form': form})

def CreateAccountLecturerView(request):
    form = CreateAccountLecturerForm(request.POST)
    if form.is_valid():
        messages.success(
            request, "Congratulations! Registration Successful, you can now log in!")
        form.save()
        return redirect('/accounts/login/')
    return render(request, 'account/register.html', {'form': form})

def CreateAccountAdminView(request):
    form = CreateAccountAdminForm(request.POST)
    if form.is_valid():
        messages.success(
            request, "Congratulations! Registration Successful, you can now log in!")
        form.save()
        return redirect('/accounts/login/')
    return render(request, 'account/register.html', {'form': form})

def CreateAccountSupplierView(request):
    form = CreateAccountSupplierForm(request.POST)
    if form.is_valid():
        messages.success(
            request, "Congratulations! Registration Successful, you can now log in!")
        form.save()
        return redirect('/accounts/login/')
    return render(request, 'account/register.html', {'form': form})

def CreateAccountNonStaffView(request):
    form = CreateAccountNonStaffForm(request.POST)
    if form.is_valid():
        messages.success(
            request, "Congratulations! Registration Successful, you can now log in!")
        form.save()
        return redirect('/accounts/login/')
    return render(request, 'account/register.html', {'form': form})

@login_required
def AddStudentsProfile(request):
    title = "Creating My New Profile To Access School services"
    button = "Add Profile"
    form = AddStudentsProfileForm(request.POST or None)
    if form.is_valid():
        user = request.user
        admission_no = form.cleaned_data['admission_no']
        full_name = form.cleaned_data['full_name']
        nationality = form.cleaned_data['nationality']
        stud_gender = form.cleaned_data['stud_gender']
        national_ID_number = form.cleaned_data['national_ID_number']
        birth_cert_no = form.cleaned_data['birth_cert_no']
        phone_number = form.cleaned_data['phone_number']
        DOB = form.cleaned_data['DOB']
        date_of_admission = form.cleaned_data['date_of_admission']
        programme = form.cleaned_data['programme']
        stage = form.cleaned_data['stage']
        postal_address = form.cleaned_data['postal_address']
        total_fees_billed = 0
        total_fees_paid = 0
        balance = 0
        reg = Students(user=user, admission_no=admission_no, full_name=full_name,
                       nationality=nationality, stud_gender=stud_gender, national_ID_number=national_ID_number,
                       birth_cert_no=birth_cert_no, phone_number=phone_number, DOB=DOB,
                       date_of_admission=date_of_admission, stage=stage, programme=programme,
                       postal_address=postal_address,total_fees_billed=total_fees_billed, total_fees_paid=total_fees_paid, balance=balance)
        reg.save()
        messages.success(request, "Profile Added Successfully")
        messages.success(request, "You Can Now Be Able To Access Services Offered To Students")
        return redirect("/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-students.html', context)


@login_required
def EditStudents(request, pk):
    title = "Edit Student"
    button = "Edit Student"
    queryset = Students.objects.get(id=pk)
    form = AddStudentsForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddStudentsForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Student Updated Successfully")
            form.save()
            return redirect("/school/all_students")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-students.html', context)


@login_required
def DeleteStudent(request, pk):
    queryset = Students.objects.get(id=pk)
    title = "Delete Student"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Student Deleted Successfully")
        return redirect("/school/all_students")
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def AddLecturerProfile(request):
    title = "Creating My User Profile"
    button = "Add Profile"
    form = AddLectureProfileForm(request.POST or None)
    if form.is_valid():
        user = request.user
        lec_no = form.cleaned_data['lec_no']
        full_name = form.cleaned_data['full_name']
        nationality = form.cleaned_data['nationality']
        lec_gender = form.cleaned_data['lec_gender']
        national_ID_number = form.cleaned_data['national_ID_number']
        phone_number = form.cleaned_data['phone_number']
        DOB = form.cleaned_data['DOB']
        postal_address = form.cleaned_data['postal_address']
        total_salary_billed = 0
        total_salary_paid = 0
        balance = 0
        reg = Lectures(user=user, lec_no=lec_no, full_name=full_name,
                       nationality=nationality, lec_gender=lec_gender, national_ID_number=national_ID_number,
                       phone_number=phone_number, DOB=DOB, postal_address=postal_address, total_salary_billed=total_salary_billed,
                       total_salary_paid=total_salary_paid,balance=balance)
        reg.save()
        messages.success(request, "Profile Added Successfully")
        messages.success(request, "You Can Now Be Able to access Services Offered To Lecturers")
        return redirect("/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-lecturers.html', context)


@login_required
def DeleteLecturer(request, pk):
    queryset = Lectures.objects.get(id=pk)
    title = "Delete Lecturer"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Lecturer Deleted Successfully")
        return redirect("/school/all_lecturers")
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def EditLecturer(request, pk):
    title = "Edit Lecturer"
    button = "Edit Lecturer"
    queryset = Lectures.objects.get(id=pk)
    form = AddLectureForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddLectureForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Lecture Updated Successfully")
            form.save()
            return redirect("/school/all_lecturers")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-lecturers.html', context)


@login_required
def AddFaculty(request):
    title = "Add New Faculty"
    button = "Add Faculty"
    form = AddFacultyForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "New Faculty Added Successfully")
        form.save()
        return redirect('/school/list-faculty')
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-faculty.html', context)


@login_required
def EditFaculty(request, pk):
    title = "Edit Faculty"
    button = "Edit Faculty"
    queryset = Faculty.objects.get(id=pk)
    form = AddFacultyForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddFacultyForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Faculty Updated Successfully")
            form.save()
            return redirect('/school/list-faculty')
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-faculty.html', context)


@login_required
def DeleteFaculty(request, pk):
    queryset = Faculty.objects.get(id=pk)
    title = "Delete Faculty"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Faculty Deleted Successfully")
        return redirect('/school/list-faculty')
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def AddGender(request):
    title = "Add New Gender"
    button = "Add Gender"
    form = AddGenderForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "New Gender Added Successfully")
        form.save()
        return redirect("/school/list-gender")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-gender.html', context)


@login_required
def EditGender(request, pk):
    title = "Edit Gender"
    button = "Edit Gender"
    queryset = Gender.objects.get(id=pk)
    form = AddGenderForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddGenderForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Gender Updated Successfully")
            form.save()
            return redirect("/school/list-gender")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-gender.html', context)


@login_required
def DeleteGender(request, pk):
    queryset = Gender.objects.get(id=pk)
    title = "Delete Gender"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Gender Deleted Successfully")
        return redirect('/school/list-gender')
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def AddProgramme(request):
    title = "Add New Programme"
    button = "Add Programme"
    form = AddProgrammesForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "New Programme Added Successfully")
        form.save()
        return redirect('/school/list-programme')
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-programmes.html', context)


@login_required
def EditProgramme(request, pk):
    title = "Edit Programme"
    button = "Edit Programme"
    queryset = Programmes.objects.get(id=pk)
    form = AddProgrammesForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddProgrammesForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Programme Updated Successfully")
            form.save()
            return redirect('/school/list-programme')
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-programmes.html', context)


@login_required
def DeleteProgramme(request, pk):
    queryset = Programmes.objects.get(id=pk)
    title = "Delete Programme"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Programme Deleted Successfully")
        return redirect('/school/list-programme')
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def AddStage(request):
    title = "Add New Stage"
    button = "Add Stage"
    form = AddStagesForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "New Stage Added Successfully")
        form.save()
        return redirect('/school/list-stage')
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-stages.html', context)


@login_required
def EditStage(request, pk):
    title = "Edit Stage"
    button = "Edit Stage"
    queryset = Stages.objects.get(id=pk)
    form = AddStagesForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddStagesForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Stage Updated Successfully")
            form.save()
            return redirect('/school/list-stage')
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-stages.html', context)


@login_required
def DeleteStage(request, pk):
    queryset = Stages.objects.get(id=pk)
    title = "Delete Stage"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Stage Deleted Successfully")
        return redirect('/school/list-stage')
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def AddUnit(request):
    title = "Add New Unit"
    button = "Add Unit"
    form = AddUnitsForm(request.POST or None)
    if form.is_valid():
        messages.success(request, "New Unit Added Successfully")
        form.save()
        return redirect('/school/list-unit')
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-units.html', context)


@login_required
def EditUnit(request, pk):
    title = "Edit Unit"
    button = "Edit Unit"
    queryset = Units.objects.get(id=pk)
    form = AddUnitsForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddUnitsForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Unit Updated Successfully")
            form.save()
            return redirect('/school/list-unit')
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-units.html', context)


@login_required
def DeleteUnit(request, pk):
    queryset = Units.objects.get(id=pk)
    title = "Delete Unit"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Unit Deleted Successfully")
        return redirect('/school/list-unit')
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def ListUnits(request):
    title = 'List of All Units'
    queryset = Units.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = Units.objects.filter(
            unit_name__icontains=form['unit_name'].value())
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-units.html", context)


@login_required
def ListProgrammes(request):
    title = 'List of All Proggrammes Offered'
    queryset = Programmes.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-programmes.html", context)


@login_required
def ListFaculty(request):
    title = 'List of Faculties In The University'
    queryset = Faculty.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = Faculty.objects.filter(
            school__icontains=form['school'].value())
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-faculty.html", context)


@login_required
def ListGender(request):
    title = 'List of All gender'
    queryset = Gender.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-gender.html", context)


@login_required
def ListStage(request):
    title = 'List of All Stages'
    queryset = Stages.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-stages.html", context)


@login_required
def ShowAddress(request):
    title = 'My Address'
    queryset = Address().objects.filter(user=request.user)
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/my-address.html", context)
