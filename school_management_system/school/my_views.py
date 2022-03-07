from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .forms2 import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime


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


@login_required
def unit_registration(request):
    title = "Unit Registration Year 1"
    button="Register Unit"
    form = UnitRegistrationForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_units1/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_units.html", context)


@login_required
def unregister_unit1(request, pk):
    queryset = marks_yr1.objects.get(id=pk)
    title = "Unregister Unit"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_units1")
    context = {
        "title": title,
        "button": button,
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
        messages.success(request, str(queryset.unit_or_subject_name)+' '+"Marks & Grade Of "+str(queryset.full_name)+' Have Been Updated Successfully')
        return redirect("/school/list_registered_units1/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update-marks.html", context)

def list_registered_units1(request):
    title = 'List of Registered Students'
    queryset = marks_yr1.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units/list_registered_units_yr1.html", context)

def my_registered_units1(request):
    title = 'MY REGISTERED UNITS OF YEAR 1'
    queryset = marks_yr1.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_units/my_registered_units_yr1.html", context)

def exam_card_yr1(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr1.objects.filter(user=request.user)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset
    }
    return render(request, "units/exam_card/exam_card_yr1.html", context)

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
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_units2/")
    context = {
        "title": title,
        "form": form,
        "button": button,
        "queryset2": queryset2
    }
    return render(request, "units/register_units.html", context)


@login_required
def unregister_unit2(request, pk):
    queryset = marks_yr2.objects.get(id=pk)
    title = "Unregister Semester 2 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_units2")
    context = {
        "title": title,
        "button": button,
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
        messages.success(request, str(queryset.unit_or_subject_name)+' '+"Marks & Grade Of "+str(queryset.full_name)+' Have Been Updated Successfully')
        return redirect("/school/list_registered_units2/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update-marks.html", context)


def list_registered_units2(request):
    title = 'List of Registered Students Semester 2'
    queryset = marks_yr2.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units/list_registered_units_yr2.html", context)

def my_registered_units2(request):
    title = 'MY REGISTERED UNITS OF YEAR 2'
    queryset = marks_yr2.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_units/my_registered_units_yr2.html", context)

def exam_card_yr2(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr2.objects.filter(user=request.user)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset
    }
    return render(request, "units/exam_card/exam_card_yr2.html", context)
#====================================================================================================

#Unit Registration 3
#==============================================================================================
@login_required
def unit_registration3(request):
    title = "Unit Registration Year 3"
    button="Register Unit"
    form = UnitRegistrationForm3(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_units3/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_units.html", context)


@login_required
def unregister_unit3(request, pk):
    queryset = marks_yr3.objects.get(id=pk)
    title = "Unregister Semester 3 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_units3")
    context = {
        "title": title,
        "button": button,
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
        messages.success(request, str(queryset.unit_or_subject_name)+' '+"Marks & Grade Of "+str(queryset.full_name)+' Have Been Updated Successfully')
        return redirect("/school/list_registered_units3/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update-marks.html", context)


def list_registered_units3(request):
    title = 'List of Registered Students Semester 3'
    queryset = marks_yr3.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units/list_registered_units_yr3.html", context)

def my_registered_units3(request):
    title = 'MY REGISTERED UNITS OF YEAR 3'
    queryset = marks_yr3.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_units/my_registered_units_yr3.html", context)

def exam_card_yr3(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr3.objects.filter(user=request.user)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset
    }
    return render(request, "units/exam_card/exam_card_yr3.html", context)
#====================================================================================================
#Unit Registration 4
#==============================================================================================
@login_required
def unit_registration4(request):
    title = "Unit Registration Year 4"
    button="Register Unit"
    form = UnitRegistrationForm4(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_units4/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_units.html", context)


@login_required
def unregister_unit4(request, pk):
    queryset = marks_yr4.objects.get(id=pk)
    title = "Unregister Semester 4 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_units4")
    context = {
        "title": title,
        "button": button,
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
        messages.success(request, str(queryset.unit_or_subject_name)+' '+"Marks & Grade Of "+str(queryset.full_name)+' Have Been Updated Successfully')
        return redirect("/school/list_registered_units4/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update-marks.html", context)


def list_registered_units4(request):
    title = 'List of Registered Students Semester 4'
    queryset = marks_yr4.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units/list_registered_units_yr4.html", context)

def my_registered_units4(request):
    title = 'MY REGISTERED UNITS OF YEAR 4'
    queryset = marks_yr4.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_units/my_registered_units_yr4.html", context)

def exam_card_yr4(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr4.objects.filter(user=request.user)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset
    }
    return render(request, "units/exam_card/exam_card_yr4.html", context)
#====================================================================================================
#Unit Registration 5
#==============================================================================================
@login_required
def unit_registration5(request):
    title = "Unit Registration Year 5"
    button="Register Unit"
    form = UnitRegistrationForm5(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_units5/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_units.html", context)

@login_required
def unregister_unit5(request, pk):
    queryset = marks_yr5.objects.get(id=pk)
    title = "Unregister Semester 5 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_units5")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks5(request, pk):
    queryset = marks_yr5.objects.get(id=pk)
    title = "Enter Unit Marks And Grades of Year 5"
    button="Add Marks"
    form = MarksForm5(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm5(request.POST or None, instance=queryset)
        form.save()
        messages.success(request, str(queryset.unit_or_subject_name)+' '+"Marks & Grade Of "+str(queryset.full_name)+' Have Been Updated Successfully')
        return redirect("/school/list_registered_units5/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update-marks.html", context)


def list_registered_units5(request):
    title = 'List of Registered Students Semester 5'
    queryset = marks_yr5.objects.all()
    context = {
        "queryset": queryset,
        "title": title,
    }
    return render(request, "units/list_registered_units/list_registered_units_yr5.html", context)

def my_registered_units5(request):
    title = 'MY REGISTERED UNITS OF YEAR 5'
    queryset = marks_yr5.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_units/my_registered_units_yr5.html", context)

def exam_card_yr5(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr5.objects.filter(user=request.user)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset
    }
    return render(request, "units/exam_card/exam_card_yr5.html", context)
#====================================================================================================
#Unit Registration 6
#==============================================================================================
@login_required
def unit_registration6(request):
    title = "Unit Registration Year 6"
    button="Register Unit"
    form = UnitRegistrationForm6(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_units6/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_units.html", context)


@login_required
def unregister_unit6(request, pk):
    queryset = marks_yr6.objects.get(id=pk)
    title = "Unregister Semester 6 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_units6")
    context = {
        "title": title,
        "button": button,
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
        messages.success(request, str(queryset.unit_or_subject_name)+' '+"Marks & Grade Of "+str(queryset.full_name)+' Have Been Updated Successfully')
        return redirect("school/list_registered_units6/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update-marks.html", context)


def list_registered_units6(request):
    title = 'List of Registered Students Semester 6'
    queryset = marks_yr6.objects.all()
    context = {
        "queryset": queryset,
        "title": title,
    }
    return render(request, "units/list_registered_units/list_registered_units_yr6.html", context)

def my_registered_units6(request):
    title = 'MY REGISTERED UNITS OF YEAR 6'
    queryset = marks_yr6.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_units/my_registered_units_yr6.html", context)

def exam_card_yr6(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr6.objects.filter(user=request.user)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset
    }
    return render(request, "units/exam_card/exam_card_yr6.html", context)
#====================================================================================================
#Unit Registration 7
#==============================================================================================
@login_required
def unit_registration7(request):
    title = "Unit Registration Year 7"
    button="Register Unit"
    form = UnitRegistrationForm7(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_or_subject_name=form.cleaned_data['unit_or_subject_name']
        instance.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_units7/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_units.html", context)


@login_required
def unregister_unit7(request, pk):
    queryset = marks_yr7.objects.get(id=pk)
    title = "Unregister Semester 7 Units"
    button="Unregister Unit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_units7/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, "school/delete_items.html", context)


@login_required
def insert_marks7(request, pk):
    queryset = marks_yr7.objects.get(id=pk)
    title = "Enter Unit Marks And Grades of Year 7"
    button="Add Marks"
    form = MarksForm7(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = MarksForm7(request.POST or None, instance=queryset)
        form.save()
        messages.success(request, str(queryset.unit_or_subject_name)+' '+"Marks & Grade Of "+str(queryset.full_name)+' Have Been Updated Successfully')
        return redirect("/school/list_registered_units7/")
    context = {
        "title": title,
        "button": button,
        "form": form
    }
    return render(request, "units/update-marks.html", context)


def list_registered_units7(request):
    title = 'List of Registered Students Semester 7'
    queryset = marks_yr7.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units/list_registered_units_yr7.html", context)

def my_registered_units7(request):
    title = 'MY REGISTERED UNITS OF YEAR 7'
    queryset = marks_yr7.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_units/my_registered_units_yr7.html", context)

def exam_card_yr7(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr7.objects.filter(user=request.user)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset
    }
    return render(request, "units/exam_card/exam_card_yr7.html", context)
#====================================================================================================
