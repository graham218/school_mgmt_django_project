from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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