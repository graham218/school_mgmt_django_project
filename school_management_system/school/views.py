import django
from django.contrib.auth.models import User
from school.models import *
from django.shortcuts import redirect, render, get_object_or_404
from .forms import AddFacultyForm, AddLectureForm, AddStudentsForm, RegistrationForm, AddressForm
from django.contrib import messages
from django.views import View
import decimal
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # for Class Based Views
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
@login_required
def home(request):
    title="Home"
    context={
        "title":title
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
            messages.success(request, "Congratulations! Registration Successful!")
            form.save()
        return render(request, 'account/register.html', {'form': form})

def AddStudents(request):
    title="Add New Students"
    form=AddStudentsForm(request.POST or None)
    if request.method=="POST":
        form=AddStudentsForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "New Student Added Successfully")
            form.save()
            #return HttpResponseRedirect("/")
    context={
        "title":title
    }
    return render(request, 'school/create-edit-students.html', context)

def EditStudents(request, pk):
    title="Edit Student"
    form=AddStudentsForm(request.POST or None, id=pk)
    if request.method=="POST":
        form=AddStudentsForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Student Updated Successfully")
            form.save()
            #return HttpResponseRedirect("/")
    context={
        "title":title
    }
    return render(request, 'school/create-edit-students.html', context)

def AddLecture(request):
    title="Add New Lectures"
    form=AddLectureForm(request.POST or None)
    if request.method=="POST":
        form=AddLectureForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Lecture Added Successfully")
            form.save()
            #return HttpResponseRedirect("/")
    context={
        "title":title
    }
    return render(request, 'school/create-edit-lectures.html', context)

def EditLecture(request, pk):
    title="Edit Lecture"
    form=AddLectureForm(request.POST or None, id=pk)
    if request.method=="POST":
        form=AddLectureForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Lecture Updated Successfully")
            form.save()
            #return HttpResponseRedirect("/")
    context={
        "title":title
    }
    return render(request, 'school/create-edit-lectures.html', context)

def AddFaculty(request):
    title="Add New Faculty"
    form=AddFacultyForm(request.POST or None)
    if request.method=="POST":
        form=AddFacultyForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Faculty Added Successfully")
            form.save()
            #return HttpResponseRedirect("/")
    context={
        "title":title
    }
    return render(request, 'school/create-edit-lectures.html', context)

def EditLecture(request, pk):
    title="Edit Lecture"
    form=AddLectureForm(request.POST or None, id=pk)
    if request.method=="POST":
        form=AddLectureForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Lecture Updated Successfully")
            form.save()
            #return HttpResponseRedirect("/")
    context={
        "title":title
    }
    return render(request, 'school/create-edit-lectures.html', context)