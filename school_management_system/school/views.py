from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.views import View

# Create your views here.
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