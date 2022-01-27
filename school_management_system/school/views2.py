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

#=====================================================================
def FeeReceiptList(request):
    title = 'List All Fee Student Receipts'
    form = FeeReceiptSearchForm(request.POST or None)
    queryset = FeeReceipt.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = FeeReceipt.objects.filter(user=form['user'].value())
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/fee_receipt_list.html", context)

@login_required
def special_exams(request):
    title = "Register For Special Exams"
    button="Register Unit"
    form = SpecialExamRegisterForm(request.POST or None)
    queryset2=SpecialExam.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "next/special_exams.html", context)

@login_required
def special_exams_marks(request, pk):
    title = "Add Marks For Special Exams"
    button="Add"
    queryset=SpecialExam.objects.get(id=pk)
    form = SpecialExamMarksForm(request.POST or None, instance=queryset)
    queryset2=SpecialExam.objects.filter(user=request.user)
    if form.is_valid():
        form = SpecialExamMarksForm(request.POST or None, instance=queryset)
        form.save()
        messages.success(request, "Marks Added Successfully")
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "next/special_exams.html", context)

def SpecialExamList(request):
    title = "Special Exams Students' List"
    form = SpecialExamSearchForm(request.POST or None)
    queryset = SpecialExam.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = SpecialExam.objects.filter(user=form['user'].value())
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/special_exams_list.html", context)

@login_required
def special_exams(request):
    title = "Register For Special Exams"
    button="Register Unit"
    form = SpecialExamRegisterForm(request.POST or None)
    queryset2=SpecialExam.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "next/special_exams.html", context)