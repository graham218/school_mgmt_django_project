from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    title="Home"
    context={
        "title":title
    }
    return render(request, "index.html", context)


# Authentication Starts Here
def RegistrationView(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        messages.success(request, "Congratulations! Registration Successful, you can now Login!")
        form.save()
    return render(request, 'account/register.html', {'form': form})