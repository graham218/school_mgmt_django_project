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