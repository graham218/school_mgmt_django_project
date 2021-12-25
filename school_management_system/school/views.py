from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    title="Home"
    context={
        "title":title
    }
    return render(request, "index.html", context)