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
    title = 'List All Fee Receipts'
    form = FeeReceiptSearchForm(request.POST or None)
    queryset = FeeReceipt.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    if request.method == 'POST':
        queryset = FeeReceipt.objects.filter(stage=form['stage'].value(), user=form['user'].value(),
                                            unit_or_subject_name=form['unit_or_subject_name'].value(), full_name__icontains=form['full_name'])
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of Registered Students.csv"'
            writer = csv.writer(response)
            writer.writerow(['USERNAME', 'STUDENT NAME', 'STAGE', 'UNIT NAME',
                            'MARKS', 'GRADE', 'DATE REAGISTERED', 'DATE UPDATED'])
            instance = queryset
            for student in instance:
                writer.writerow([student.user, student.full_name, student.stage,
                                 student.unit_or_subject_name, student.marks, student.grade,
                                 student.date_created, student.date_updated])
            return response

    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_units.html", context)