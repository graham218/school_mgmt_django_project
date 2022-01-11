import django
from django.contrib.auth.models import User
from school.models import *
from .forms import *
from django.shortcuts import redirect, render, get_object_or_404
from .forms import AddFacultyForm, AddGenderForm, AddLectureForm, AddProgrammesForm, AddStagesForm, AddStudentsForm, AddUnitsForm, RegistrationForm, AddressForm
from django.contrib import messages
from django.views import View
import csv
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

@login_required
def AddAddress(request):
    title = "Add Address"
    form = AddressForm(request.POST or None)
    if request.method == "POST":
        form = AddressForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "Profile Updated Successfully")
            form.save()
            return HttpResponseRedirect("/")
    context = {
        "title": title
    }
    return render(request, 'account/profile.html', context)

@login_required
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

@login_required
def DeleteAddress(request, pk):
    queryset = Address.objects.get(id=pk)
    title="Delete Address"
    if request.method=="POST":
        queryset.delete()
        messages.success(request,"Address Deleted Successfully")
        #return HttpResponseRedirect()
    context={
        "title": title
    }
    return render(request, "school/delete_items.html", context)

@login_required
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

@login_required
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

@login_required
def DeleteStudent(request, pk):
    queryset = Students.objects.get(id=pk)
    title="Delete Student"
    if request.method=="POST":
        queryset.delete()
        messages.success(request,"Student Deleted Successfully")
        #return HttpResponseRedirect()
    context={
        "title": title
    }
    return render(request, "school/delete_items.html", context)

@login_required
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

@login_required
def DeleteLecturer(request, pk):
    queryset = Lectures.objects.get(id=pk)
    title="Delete Lecturer"
    if request.method=="POST":
        queryset.delete()
        messages.success(request,"Lecturer Deleted Successfully")
        #return HttpResponseRedirect()
    context={
        "title": title
    }
    return render(request, "school/delete_items.html", context)

@login_required
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

@login_required
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

@login_required
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

@login_required
def DeleteFaculty(request, pk):
    queryset = Faculty.objects.get(id=pk)
    title="Delete Faculty"
    if request.method=="POST":
        queryset.delete()
        messages.success(request,"Faculty Deleted Successfully")
        #return HttpResponseRedirect()
    context={
        "title": title
    }
    return render(request, "school/delete_items.html", context)

@login_required
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

@login_required
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

@login_required
def DeleteGender(request, pk):
    queryset = Gender.objects.get(id=pk)
    title="Delete Gender"
    if request.method=="POST":
        queryset.delete()
        messages.success(request,"Gender Deleted Successfully")
        #return HttpResponseRedirect()
    context={
        "title": title
    }
    return render(request, "school/delete_items.html", context)

@login_required
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

@login_required
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

@login_required
def DeleteProgramme(request, pk):
    queryset = Programmes.objects.get(id=pk)
    title="Delete Programme"
    if request.method=="POST":
        queryset.delete()
        messages.success(request,"Programme Deleted Successfully")
        #return HttpResponseRedirect()
    context={
        "title": title
    }
    return render(request, "school/delete_items.html", context)

@login_required
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

@login_required
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

@login_required
def DeleteStage(request, pk):
    queryset = Stages.objects.get(id=pk)
    title="Delete Stage"
    if request.method=="POST":
        queryset.delete()
        messages.success(request,"Stage Deleted Successfully")
        #return HttpResponseRedirect()
    context={
        "title": title
    }
    return render(request, "school/delete_items.html", context)

@login_required
def AddUnit(request):
    title = "Add New Unit"
    button = "Add Unit"
    form = AddUnitsForm(request.POST or None)
    if request.method == "POST":
        form = AddUnitsForm(request.POST or None)
        if form.is_valid():
            messages.success(request, "New Unit Added Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-units.html', context)

@login_required
def EditUnit(request, pk):
    title = "Edit Unit"
    button = "Edit Unit"
    form = AddUnitsForm(request.POST or None, id=pk)
    if request.method == "POST":
        form = AddUnitsForm(request.POST or None, id=pk)
        if form.is_valid():
            messages.success(request, "Unit Updated Successfully")
            form.save()
            # return HttpResponseRedirect("/")
    context = {
        "title": title,
        "button": button
    }
    return render(request, 'school/create-edit-units.html', context)

@login_required
def DeleteUnit(request, pk):
    queryset = Units.objects.get(id=pk)
    title="Delete Unit"
    if request.method=="POST":
        queryset.delete()
        messages.success(request,"Unit Deleted Successfully")
        #return HttpResponseRedirect()
    context={
        "title": title
    }
    return render(request, "school/delete_items.html", context)

@login_required
def ListStudents(request):
	title = 'List of All Students'
	form = StudentSearchForm(request.POST or None)
	queryset = Students.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	if request.method == 'POST':
		queryset = Students.objects.filter(admission_no__icontains=form['admission_no'].value(),
										full_name__icontains=form['full_name'].value(),
                                        programme__icontains=form['programme'].value()
										)
		if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
			writer = csv.writer(response)
			writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
			instance = queryset
			for stock in instance:
				writer.writerow([stock.category, stock.item_name, stock.quantity])
			return response
	
	context = {
	"form": form,
	"title": title,
	"queryset": queryset,
	}
	return render(request, "school/list-students.html", context)