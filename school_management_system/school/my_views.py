from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def UserProfile(request):
    title="Student's Profile"
    title2="Lecturer's Profile"
    my_queryset=Students.objects.get(user=request.user)
    lec_queryset=Lectures.objects.get(user=request.user)
    context={
        "title": title,
        "title2": title2,
        "my_queryset": my_queryset,
        "lec_queryset": lec_queryset
    }
    return render(request, "navbar.html", context)