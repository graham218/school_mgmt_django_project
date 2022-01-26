from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .forms2 import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm


@login_required
def EditStudentsProfile(request, pk):
    title = "Edit Profile"
    button = "Edit Profile"
    queryset = Students.objects.get(id=pk)
    form = EditStudentsForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = EditStudentsForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Student Updated Successfully")
            form.save()
            return redirect("/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-students.html', context)


@login_required
def EditLecturerProfile(request, pk):
    title = "Edit Profile"
    button = "Edit Profile"
    queryset = Lectures.objects.get(id=pk)
    form = EditLectureForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = EditLectureForm(request.POST or None, instance=queryset)
        if form.is_valid():
            messages.success(request, "Lecturer Updated Successfully")
            form.save()
            return redirect("/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, 'school/create-edit-lecturers.html', context)

# paypal payment view


def payment_process(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '100',
        'item_name': 'Item_Name_xyz',
        'invoice': 'Test Payment Invoice',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'pets/payment_process.html', {'form': form})


@login_required
def unit_registration(request):
    title = "Unit Registration Year 1"
    button="Register Unit"
    form = UnitRegistrationForm(request.POST or None)
    queryset2=marks_yr1.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/unit_registration/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "units/unit_registration.html", context)


@login_required
def unregister_unit(request, pk):
    queryset = marks_yr1.objects.get(id=pk)
    queryset2=marks_yr1.objects.filter(user=request.user)
    title = "Unregister Unit"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/list_registered_units")
    context = {
        "title": title,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks(request, pk):
    queryset = marks_yr1.objects.get(id=pk)
    title = "Enter Unit Marks And Grades"
    button="Add Marks"
    form = MarksForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm(request.POST or None, instance=queryset)
        form.save()
        return redirect("/school/list_registered_units/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update_marks.html", context)


def list_registered_units(request):
    title = 'List of Registered Students'
    form = MarksSearch(request.POST or None)
    queryset = marks_yr1.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = marks_yr1.objects.filter(stage=form['stage'].value(), user=form['user'].value(),
                                            unit_or_subject_name=form['unit_or_subject_name'].value(), full_name__icontains=form['full_name'])
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Registered Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USERNAME', 'STUDENT NAME', 'STAGE', 'UNIT NAME',
                            'MARKS', 'GRADE', 'DATE REAGISTERED', 'DATE UPDATED'])
            instance = queryset
            for student in instance:
                writer.writerow([student.user, student.full_name, student.stage,
                                 student.unit_or_subject_name, student.marks, student.grade,
                                 student.date_created, student.date_updated])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units.html", context)

#==============================================================================================
@login_required
def unit_registration2(request):
    title = "Unit Registration Year 2"
    button="Register Unit"
    form = UnitRegistrationForm2(request.POST or None)
    queryset2=marks_yr2.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/unit_registration/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "units/unit_registration.html", context)


@login_required
def unregister_unit2(request, pk):
    queryset = marks_yr2.objects.get(id=pk)
    queryset2=marks_yr2.objects.filter(user=request.user)
    title = "Unregister Semester 2 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/list_registered_units")
    context = {
        "title": title,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks2(request, pk):
    queryset = marks_yr2.objects.get(id=pk)
    title = "Enter Unit Marks And Grades of Year 2"
    button="Add Marks"
    form = MarksForm2(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm2(request.POST or None, instance=queryset)
        form.save()
        return redirect("/school/list_registered_units/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update_marks.html", context)


def list_registered_units2(request):
    title = 'List of Registered Students Semester 2'
    form = MarksSearch2(request.POST or None)
    queryset = marks_yr2.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = marks_yr2.objects.filter(stage=form['stage'].value(), user=form['user'].value(),
                                            unit_or_subject_name=form['unit_or_subject_name'].value(), full_name__icontains=form['full_name'])
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Registered Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USERNAME', 'STUDENT NAME', 'STAGE', 'UNIT NAME',
                            'MARKS', 'GRADE', 'DATE REAGISTERED', 'DATE UPDATED'])
            instance = queryset
            for student in instance:
                writer.writerow([student.user, student.full_name, student.stage,
                                 student.unit_or_subject_name, student.marks, student.grade,
                                 student.date_created, student.date_updated])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units.html", context)
#====================================================================================================

#Unit Registration 3
#==============================================================================================
@login_required
def unit_registration3(request):
    title = "Unit Registration Year 3"
    button="Register Unit"
    form = UnitRegistrationForm3(request.POST or None)
    queryset2=marks_yr3.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/unit_registration/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "units/unit_registration.html", context)


@login_required
def unregister_unit3(request, pk):
    queryset = marks_yr3.objects.get(id=pk)
    queryset2=marks_yr3.objects.filter(user=request.user)
    title = "Unregister Semester 3 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/list_registered_units")
    context = {
        "title": title,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks3(request, pk):
    queryset = marks_yr3.objects.get(id=pk)
    title = "Enter Unit Marks And Grades of Year 3"
    button="Add Marks"
    form = MarksForm3(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm3(request.POST or None, instance=queryset)
        form.save()
        return redirect("/school/list_registered_units/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update_marks.html", context)


def list_registered_units3(request):
    title = 'List of Registered Students Semester 3'
    form = MarksSearch3(request.POST or None)
    queryset = marks_yr3.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = marks_yr3.objects.filter(stage=form['stage'].value(), user=form['user'].value(),
                                            unit_or_subject_name=form['unit_or_subject_name'].value(), full_name__icontains=form['full_name'])
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Registered Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USERNAME', 'STUDENT NAME', 'STAGE', 'UNIT NAME',
                            'MARKS', 'GRADE', 'DATE REAGISTERED', 'DATE UPDATED'])
            instance = queryset
            for student in instance:
                writer.writerow([student.user, student.full_name, student.stage,
                                 student.unit_or_subject_name, student.marks, student.grade,
                                 student.date_created, student.date_updated])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units.html", context)
#====================================================================================================
#Unit Registration 4
#==============================================================================================
@login_required
def unit_registration4(request):
    title = "Unit Registration Year 4"
    button="Register Unit"
    form = UnitRegistrationForm4(request.POST or None)
    queryset2=marks_yr4.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/unit_registration/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "units/unit_registration.html", context)


@login_required
def unregister_unit4(request, pk):
    queryset = marks_yr4.objects.get(id=pk)
    queryset2=marks_yr4.objects.filter(user=request.user)
    title = "Unregister Semester 4 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/list_registered_units")
    context = {
        "title": title,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks4(request, pk):
    queryset = marks_yr4.objects.get(id=pk)
    title = "Enter Unit Marks And Grades of Year 4"
    button="Add Marks"
    form = MarksForm4(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm4(request.POST or None, instance=queryset)
        form.save()
        return redirect("/school/list_registered_units/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update_marks.html", context)


def list_registered_units4(request):
    title = 'List of Registered Students Semester 4'
    form = MarksSearch4(request.POST or None)
    queryset = marks_yr4.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = marks_yr4.objects.filter(stage=form['stage'].value(), user=form['user'].value(),
                                            unit_or_subject_name=form['unit_or_subject_name'].value(), full_name__icontains=form['full_name'])
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Registered Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USERNAME', 'STUDENT NAME', 'STAGE', 'UNIT NAME',
                            'MARKS', 'GRADE', 'DATE REAGISTERED', 'DATE UPDATED'])
            instance = queryset
            for student in instance:
                writer.writerow([student.user, student.full_name, student.stage,
                                 student.unit_or_subject_name, student.marks, student.grade,
                                 student.date_created, student.date_updated])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units.html", context)
#====================================================================================================
#Unit Registration 5
#==============================================================================================
@login_required
def unit_registration5(request):
    title = "Unit Registration Year 5"
    button="Register Unit"
    form = UnitRegistrationForm5(request.POST or None)
    queryset2=marks_yr5.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/unit_registration/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "units/unit_registration.html", context)


@login_required
def unregister_unit5(request, pk):
    queryset = marks_yr5.objects.get(id=pk)
    queryset2=marks_yr5.objects.filter(user=request.user)
    title = "Unregister Semester 5 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/list_registered_units")
    context = {
        "title": title,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks4(request, pk):
    queryset = marks_yr5.objects.get(id=pk)
    title = "Enter Unit Marks And Grades of Year 5"
    button="Add Marks"
    form = MarksForm5(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm5(request.POST or None, instance=queryset)
        form.save()
        return redirect("/school/list_registered_units/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update_marks.html", context)


def list_registered_units5(request):
    title = 'List of Registered Students Semester 5'
    form = MarksSearch5(request.POST or None)
    queryset = marks_yr5.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = marks_yr5.objects.filter(stage=form['stage'].value(), user=form['user'].value(),
                                            unit_or_subject_name=form['unit_or_subject_name'].value(), full_name__icontains=form['full_name'])
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Registered Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USERNAME', 'STUDENT NAME', 'STAGE', 'UNIT NAME',
                            'MARKS', 'GRADE', 'DATE REAGISTERED', 'DATE UPDATED'])
            instance = queryset
            for student in instance:
                writer.writerow([student.user, student.full_name, student.stage,
                                 student.unit_or_subject_name, student.marks, student.grade,
                                 student.date_created, student.date_updated])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units.html", context)
#====================================================================================================
#Unit Registration 6
#==============================================================================================
@login_required
def unit_registration6(request):
    title = "Unit Registration Year 6"
    button="Register Unit"
    form = UnitRegistrationForm4(request.POST or None)
    queryset2=marks_yr6.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/unit_registration/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "units/unit_registration.html", context)


@login_required
def unregister_unit6(request, pk):
    queryset = marks_yr6.objects.get(id=pk)
    queryset2=marks_yr6.objects.filter(user=request.user)
    title = "Unregister Semester 6 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/list_registered_units")
    context = {
        "title": title,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks6(request, pk):
    queryset = marks_yr6.objects.get(id=pk)
    title = "Enter Unit Marks And Grades of Year 6"
    button="Add Marks"
    form = MarksForm6(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm6(request.POST or None, instance=queryset)
        form.save()
        return redirect("/school/list_registered_units/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update_marks.html", context)


def list_registered_units6(request):
    title = 'List of Registered Students Semester 6'
    form = MarksSearch6(request.POST or None)
    queryset = marks_yr6.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = marks_yr6.objects.filter(stage=form['stage'].value(), user=form['user'].value(),
                                            unit_or_subject_name=form['unit_or_subject_name'].value(), full_name__icontains=form['full_name'])
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Registered Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USERNAME', 'STUDENT NAME', 'STAGE', 'UNIT NAME',
                            'MARKS', 'GRADE', 'DATE REAGISTERED', 'DATE UPDATED'])
            instance = queryset
            for student in instance:
                writer.writerow([student.user, student.full_name, student.stage,
                                 student.unit_or_subject_name, student.marks, student.grade,
                                 student.date_created, student.date_updated])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units.html", context)
#====================================================================================================
