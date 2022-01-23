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
    queryset=Students.objects.get(id=pk)
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
    queryset=Lectures.objects.get(id=pk)
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

#paypal payment view
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

def unit_registration(request):
    