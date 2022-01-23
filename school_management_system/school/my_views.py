from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
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
    title = "Unit Registration"
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
