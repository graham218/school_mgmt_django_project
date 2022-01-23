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
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


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
                    #messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("/accounts/password-reset/done/")
    form = PasswordResetForm()
    return render(request=request, template_name="account/password_reset.html", context={"form": form})

# Create your views here.


@login_required
def home(request):
    title = "Home"
    title1 = "Student's Profile"
    title2 = "Lecturer's Profile"
    my_queryset = Students.objects.filter(user=request.user)
    # lec_queryset=Lectures.objects.get(user=request.user)
    context = {
        "title": title,
        "title1": title1,
        "title2": title2,
        "my_queryset": my_queryset,
        # "lec_queryset": lec_queryset
    }
    return render(request, "index.html", context)


# Authentication Starts Here


def RegistrationView(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        messages.success(
            request, "Congratulations! Registration Successful, you can now log in!")
        form.save()
        return redirect('/accounts/register/')
    return render(request, 'account/register.html', {'form': form})


@login_required
def AddAddress(request):
    title = "Add Address"
    button = "Add Address"
    form = AddressForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Address Updated Successfully")
        return redirect("/")
    context = {
        "title": title,
        "form": form,
        "button": button
    }
    return render(request, 'school/create-edit-address.html', context)


@login_required
def UpdateAddress(request, pk):
    title = "Update Address"
    button = "Update Address"
    queryset = Address.objects.get(id=pk)
    form = AddressForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddressForm(request.POST or None, id=pk)
        if form.is_valid():
            form.save()
            messages.success(request, "Address Updated Successfully")
            return redirect("/")
    context = {
        "title": title,
        "form": form,
        "button": button
    }
    return render(request, 'school/create-edit-address.html', context)


@login_required
def DeleteAddress(request, pk):
    queryset = Address.objects.get(id=pk)
    title = "Delete Address"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Address Deleted Successfully")
        return redirect()
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def AddStudents(request):
    title = "Add New Students"
    button = "Add Student"
    form = AddStudentsForm(request.POST or None, request.FILES)
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
        date_of_graduation = form.cleaned_data['date_of_graduation']
        programme = form.cleaned_data['programme']
        stage = form.cleaned_data['stage']
        profile_photo = form.cleaned_data['profile_photo']
        postal_address = form.cleaned_data['postal_address']
        school_email = form.cleaned_data['school_email']
        school_email_password = form.cleaned_data['school_email_password']
        total_fees_billed = form.cleaned_data['total_fees_billed']
        total_fees_paid = form.cleaned_data['total_fees_paid']
        balance = form.cleaned_data['balance']
        reg = Students(user=user, admission_no=admission_no, full_name=full_name,
                       nationality=nationality, stud_gender=stud_gender, national_ID_number=national_ID_number,
                       birth_cert_no=birth_cert_no, phone_number=phone_number, DOB=DOB,
                       date_of_admission=date_of_admission, stage=stage, date_of_graduation=date_of_graduation,
                       programme=programme, profile_photo=profile_photo,
                       postal_address=postal_address, school_email=school_email, school_email_password=school_email_password,
                       total_fees_billed=total_fees_billed, total_fees_paid=total_fees_paid, balance=balance)
        reg.save()
        messages.success(request, "New Student Added Successfully")
        return redirect("/school/list-students")
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
            return redirect("/school/list-students")
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
        return redirect("/school/list-students")
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def AddLecturer(request):
    title = "Add New Lecturer"
    button = "Add Lecture"
    form = AddLectureForm(request.POST or None, request.FILES)
    if form.is_valid():
        user = request.user
        lec_no = form.cleaned_data['lec_no']
        full_name = form.cleaned_data['full_name']
        nationality = form.cleaned_data['nationality']
        lec_gender = form.cleaned_data['lec_gender']
        national_ID_number = form.cleaned_data['national_ID_number']
        phone_number = form.cleaned_data['phone_number']
        DOB = form.cleaned_data['DOB']
        profile_photo = form.cleaned_data['profile_photo']
        postal_address = form.cleaned_data['postal_address']
        school_email = form.cleaned_data['school_email']
        school_email_password = form.cleaned_data['school_email_password']
        total_salary_billed = form.cleaned_data['total_salary_billed']
        total_salary_paid = form.cleaned_data['total_salary_paid']
        balance = form.cleaned_data['balance']
        reg = Lectures(user=user, lec_no=lec_no, full_name=full_name,
                       nationality=nationality, lec_gender=lec_gender, national_ID_number=national_ID_number,
                       phone_number=phone_number, DOB=DOB, profile_photo=profile_photo,
                       postal_address=postal_address, school_email=school_email, school_email_password=school_email_password,
                       total_salary_billed=total_salary_billed, total_salary_paid=total_salary_paid, balance=balance)
        reg.save()
        messages.success(request, "New Lecture Added Successfully")
        return redirect("/school/list-lecturer")
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
        return redirect("/school/list-lecturer")
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def EditLecturer(request, pk):
    title = "Edit Lecturer"
    button = "Edit Lecturer"
    queryset = Lectures.objects.get(id=pk)
    form = AddLectureForm(
        request.FILES, request.POST or None, instance=queryset)
    if request.method == "POST":
        form = AddLectureForm(
            request.FILES, request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Lecture Updated Successfully")
            form.save()
            return redirect("/school/list-lecturer")
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
def ListStudents(request):
    title = 'List of All Students'
    form = StudentSearchForm(request.POST or None)
    queryset = Students.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = Students.objects.filter(admission_no__icontains=form['admission_no'].value(),
                                           full_name__icontains=form['full_name'].value(
        ),
            programme=form['programme'].value()
        )
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USER', 'ADMISSION MUMBER', 'FULL NAME', 'NATIONALITY',
                             'GENDER', 'N.ID NUMBER', 'BIRTH CERT NO', 'PHONE NO', 'DOB', 'DATE OF ADMISSION',
                             'PROGRAMME', 'STAGE', 'POSTAL ADDRESS', 'FEE BALANCE'])
            instance = queryset
            for students in instance:
                writer.writerow([students.user, students.admission_no, students.full_name,
                                 students.nationality, students.stud_gender, students.national_ID_number,
                                 students.birth_cert_no, students.phone_number, students.DOB,
                                 students.date_of_admission, students.programme, students.stage,
                                 students.postal_address, students.balance])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-students.html", context)


@login_required
def Listlectures(request):
    title = 'List of All Lectures'
    form = LecturerSearchForm(request.POST or None)
    queryset = Lectures.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = Lectures.objects.filter(lec_no__icontains=form['lec_no'].value(),
                                           full_name__icontains=form['full_name'].value(
        ),
            national_ID_number__icontains=form['national_ID_number'].value(
        )
        )
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USER', 'LEC MUMBER', 'FULL NAME', 'NATIONALITY',
                             'GENDER', 'N.ID NUMBER', 'PHONE NO', 'DOB', 'POSTAL ADDRESS', 'SALARY BALANCE'])
            instance = queryset
            for lecturer in instance:
                writer.writerow([lecturer.user, lecturer.lec_no, lecturer.full_name,
                                 lecturer.nationality, lecturer.lec_gender, lecturer.national_ID_number,
                                 lecturer.phone_number, lecturer.DOB, lecturer.postal_address, lecturer.balance])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-lecturers.html", context)


@login_required
def ListUnits(request):
    title = 'List of All Units'
    form = UnitSearchForm(request.POST or None)
    queryset = Units.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = Units.objects.filter(
            unit_name__icontains=form['unit_name'].value())
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-units.html", context)


@login_required
def ListProgrammes(request):
    title = 'List of All Proggrammes Offered'
    form = ProgrammeSearchForm(request.POST or None)
    queryset = Programmes.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = Programmes.objects.filter(name__icontains=form['name'].value(),
                                             faculty=form['faculty'].value())
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "school/list-programmes.html", context)


@login_required
def ListFaculty(request):
    title = 'List of Faculties In The University'
    form = FacultySearchForm(request.POST or None)
    queryset = Faculty.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = Faculty.objects.filter(
            school__icontains=form['school'].value())
    context = {
        "form": form,
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
