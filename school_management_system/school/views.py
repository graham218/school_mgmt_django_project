import django
from django.contrib.auth.models import User
from school.models import *
from django.shortcuts import redirect, render, get_object_or_404
from .forms import AddFacultyForm, AddGenderForm, AddLectureForm, AddProgrammesForm, AddStagesForm, AddStudentsForm, AddUnitsForm, RegistrationForm, AddressForm
from django.contrib import messages
from django.views import View
import decimal
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator  # for Class Based Views
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
@login_required
def home(request):
    title = "Home"
    context = {
        "title": title
    }
    return render(request, "index.html", context)


# Authentication Starts Here

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, "Congratulations! Registration Successful!")
            form.save()
        return render(request, 'account/register.html', {'form': form})


def AddAddress(request):
    title = "Add Address"
    form = AddressForm(request.POST or None)
    if request.method == "POST":
        form = AddressForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "Profile Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title
    }
    return render(request, 'account/profile.html', context)


def UpdateAddress(request, pk):
    title = "Update Address"
    form = AddressForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddressForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Address Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title
    }
    return render(request, 'account/profile.html', context)


def DeleteAddress(request, pk):
    queryset = Address.objects.get(user=request.user, id=pk)
    queryset.delete()


def AddStudents(request):
    title = "Add New Students"
    button="Add Student"
    form = AddStudentsForm(request.POST or None)
    if request.method == "POST":
        form = AddStudentsForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Student Added Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-students.html', context)


def EditStudents(request, pk):
    title = "Edit Student"
    button = "Edit Student"
    form = AddStudentsForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddStudentsForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Student Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-students.html', context)


def AddLecturer(request):
    title = "Add New Lecturer"
    button="Add Lecture"
    form = AddLectureForm(request.POST or None)
    if request.method == "POST":
        form = AddLectureForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Lecture Added Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-lecturers.html', context)


def EditLecturer(request, pk):
    title = "Edit Lecturer"
    button = "Edit Lecturer"
    form = AddLectureForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddLectureForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Lecture Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-lecturers.html', context)


def AddFaculty(request):
    title = "Add New Faculty"
    button="Add Faculty"
    form = AddFacultyForm(request.POST or None)
    if request.method == "POST":
        form = AddFacultyForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Faculty Added Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-faculty.html', context)


def EditFaculty(request, pk):
    title = "Edit Faculty"
    button="Edit Faculty"
    form = AddFacultyForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddFacultyForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Faculty Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-faculty.html', context)


def AddGender(request):
    title = "Add New Gender"
    button="Add Gender"
    form = AddGenderForm(request.POST or None)
    if request.method == "POST":
        form = AddGenderForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Gender Added Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-gender.html', context)


def EditGender(request, pk):
    title = "Edit Gender"
    button = "Edit Gender"
    form = AddGenderForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddGenderForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Gender Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-gender.html', context)


def AddProgramme(request):
    title = "Add New Programme"
    button = "Add Programme"
    form = AddProgrammesForm(request.POST or None)
    if request.method == "POST":
        form = AddProgrammesForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Programme Added Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-programmes.html', context)


def EditProgramme(request, pk):
    title = "Edit Programme"
    button="Edit Programme"
    form = AddProgrammesForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddProgrammesForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Programme Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-programmes.html', context)


def AddStage(request):
    title = "Add New Stage"
    button = "Add Stage"
    form = AddStagesForm(request.POST or None)
    if request.method == "POST":
        form = AddStagesForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Stage Added Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-stages.html', context)


def EditStage(request, pk):
    title = "Edit Stage"
    button = "Edit Stage"
    form = AddStagesForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddStagesForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Stage Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-stages.html', context)


def AddUnit(request):
    title = "Add New Unit"
    form = AddUnitsForm(request.POST or None)
    if request.method == "POST":
        form = AddUnitsForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Unit Added Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title
    }
    return render(request, 'school/create-edit-units.html', context)


def EditUnit(request, pk):
    title = "Edit Unit"
    form = AddUnitsForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddUnitsForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Unit Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title
    }
    return render(request, 'school/create-edit-units.html', context)
