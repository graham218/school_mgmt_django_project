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
    if request.method=="POST":
        form = SpecialExamMarksForm(request.POST or None, instance=queryset)
        if form.is_valid():
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
def lecturer_units(request):
    title = "Register For Special Exams"
    button="Register Unit"
    form = LecturerUnitsForm(request.POST or None)
    form2 = LecturerUnitsSearchForm(request.POST or None)
    queryset2=LecturerUnits.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.unit_name=form.cleaned_data['unit_name']
        instance.level_of_understanding=form.cleaned_data['level_of_understanding']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "form2": form2,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "next/lecturer_units.html", context)

@login_required
def lecturer_units_edit(request, pk):
    title = "Update Units"
    button="Update Unit"
    queryset=LecturerUnits.objects.get(id=pk)
    form = LecturerUnitsForm(request.POST or None, instance=queryset)
    form2 = LecturerUnitsSearchForm(request.POST or None)
    queryset2=LecturerUnits.objects.filter(user=request.user)
    if request.method=="POST":
        form = LecturerUnitsForm(request.POST or None, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Unit Updated Successfully")
            return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "form2": form2,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "next/lecturer_units.html", context)

@login_required
def lecturer_units_delete(request, pk):
    title = "Delete Unit"
    button="Delete Unit"
    queryset=LecturerUnits.objects.get(id=pk)
    if request.method=="POST":
        queryset.delete()
        messages.error(request, "Unit Deleted From My List")
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "school/delete_items.html", context)

def ListAllLecturerUnits(request):
    title = "List Of All Lecturers' Units"
    form = LecturerUnitsSearchForm(request.POST or None)
    queryset = LecturerUnits.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = LecturerUnits.objects.filter(user=form['user'].value())
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/lecturer_unit_list.html", context)

#=================================================================================
#Seats
@login_required
def seats(request):
    title = "Add New Seats/Positions For Students To Vie"
    button="Add Seat"
    form = SeatsForm(request.POST or None)
    queryset=Seats.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, "Seat/Position Added Successfully")
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset": queryset
    }
    return render(request, "next/seats.html", context)

@login_required
def seats_edit(request, pk):
    title = "Edit Existing Seats/Positions For Students To Vie"
    button="Add Seat"
    queryset2=Seats.objects.get(id=pk)
    form = SeatsForm(request.POST or None, instance=queryset2)
    queryset=Seats.objects.all()
    if request.method=="POST":
        form = SeatsForm(request.POST or None, instance=queryset2)
        if form.is_valid():
            form.save()
            messages.success(request, "Seat/Position Updated Successfully")
            return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset": queryset
    }
    return render(request, "next/seats.html", context)

@login_required
def seats_delete(request, pk):
    title = "Delete Seat"
    button="Delete Seat"
    queryset2=Seats.objects.get(id=pk)
    if request.method=="POST":
        queryset2.delete()
        messages.error(request, "Seat/Position Deleted From Database")
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset": queryset
    }
    return render(request, "next/seats.html", context)

#==========================================================================================
#Notice Board
@login_required
def add_notice(request):
    title = "Add Notice"
    button="Add Notice"
    form = NoticeBoardForm(request.POST or None)
    form2 = NoticeBoardSearchForm(request.POST or None)
    queryset2=NoticeBoard.objects.filter(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.written_by=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.notice=form.cleaned_data['notice']
        instance.signature=form.cleaned_data['signature']
        instance.save()
        messages.success(request, "Notice Added Successfully on Board")
        return HttpResponseRedirect("/")
    context = {
        "title": title,
        "form": form,
        "form2": form2,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "next/add_notice.html", context)

