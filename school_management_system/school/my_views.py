from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.http import HttpResponse
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
    title = "Unit Registration"
    form = UnitRegistrationForm(request.POST or None)
    if form.is_valid():
        user = request.user,
        full_name = request.user.get_fullname,
        stage = form.cleaned_data['full_name'],
        unit_or_subject_name = form.cleaned_data['unit_or_subject_name'],
        reg = marks_yr1(user=user, full_name=full_name, stage=stage,
                        unit_or_subject_name=unit_or_subject_name)
        reg.save()
        messages.success(request, "Unit Registered Successfully")
        return redirect("/")
    context = {
        "title": title,
        "form": form
    }
    return render(request, "units/unit_registration.html", context)


@login_required
def unregister_unit(request, pk):
    queryset = marks_yr1.objects.get(id=pk)
    title = "Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Unit Unregistered Successfully")
        return redirect("/")
    context = {
        "title": title
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks(request, pk):
    queryset = marks_yr1.objects.get(id=pk)
    title = "Enter Unit Marks And Grades"
    form = MarksForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm(request.POST or None, instance=queryset)
        form.save()
        return redirect("/")
    context = {
        "title": title,
        "form": form
    }
    return render(request, "units/unit_registration.html", context)


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
