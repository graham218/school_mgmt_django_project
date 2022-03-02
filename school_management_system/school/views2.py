from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .forms2 import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.urls import reverse

# =====================================================================

@login_required
def compose_notices(request):
    title='Compose Notice To Reach Everyone'
    context={
        'title':title
    }
    return render(request, 'notifications/compose_notice.html', context)

@login_required
def all_public_notices(request):
    title='All Public Notices'
    context={
        'title':title
    }
    return render(request, 'notifications/all_public_notices.html', context)

@login_required
def read_public_notices(request):
    title='All Public Notices'
    context={
        'title':title
    }
    return render(request, 'notifications/read_public_notices.html', context)

@login_required
def FeeReceiptList(request):
    title = 'List All Fee Student Receipts'
    queryset = FeeReceipt.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/fee_receipt_list.html", context)

@login_required
def unit_year_page(request):
    title="Choose Your Year Of Study"
    context={
        "title":title
    }
    return render(request, "units/year_page.html", context)

@login_required
def unit_year_page_marks(request):
    title="Choose Your Year Of Study"
    context={
        "title":title
    }
    return render(request, "units/pages/year_page_marks.html", context)

@login_required
def resit_year_page(request):
    title="Choose Your Year Of Study To Register Resits/Retakes/Special Exams"
    context={
        "title":title
    }
    return render(request, "units/pages/resit_year_page.html", context)

@login_required
def resit_year_page_marks(request):
    title="Choose Year Of Study To Enter Marks And Grades"
    context={
        "title":title
    }
    return render(request, "units/pages/resit_year_page_marks.html", context)

@login_required
def register_special_exams(request):
    title = "Register For Special Exams"
    button = "Register Unit"
    form = SpecialExamRegisterForm(request.POST or None)
    if form.is_valid():
        user = request.user
        full_name = request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        stage = form.cleaned_data['stage']
        unit_name = form.cleaned_data['unit_name']
        reg=SpecialExam(user=user,full_name=full_name,stage=stage, unit_name=unit_name)
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/my_special_exams")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "next/register_special_exams.html", context)


def my_special_exams(request):
    title = "My Registered Special Exams"
    queryset = SpecialExam.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/my_special_exams.html", context)


@login_required
def special_exams_marks(request, pk):
    title = "Add Marks For Special Exams"
    button = "Add Marks"
    queryset = SpecialExam.objects.get(id=pk)
    form = SpecialExamMarksForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = SpecialExamMarksForm(request.POST or None, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Marks Added Successfully")
            return HttpResponseRedirect("/school/SpecialExamList")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "next/register_special_exams.html", context)


@login_required
def delete_special_exams(request, pk):
    title = "Delete Special Exams"
    button = "Delete"
    queryset = SpecialExam.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Unregistered from Special Exams")
        return HttpResponseRedirect("/school/my_special_exams")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def SpecialExamList(request):
    title = "Special Exams Students' List"
    queryset = SpecialExam.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/special_exams_list.html", context)


@login_required
def add_lecturer_units(request):
    title = "Add Units"
    button = "Add Unit"
    form = LecturerUnitsForm(request.POST or None)
    if form.is_valid():
        username = request.user
        full_name = request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        unit_name = form.cleaned_data['unit_name']
        level_of_understanding = form.cleaned_data['level_of_understanding']
        reg=LecturerUnits(unit_name=unit_name,username=username,full_name=full_name,level_of_understanding=level_of_understanding)
        reg.save()
        messages.success(request, "Unit Registered Successfully")
        return HttpResponseRedirect("/school/ListAllLecturerUnits")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "next/create_edit_lecturer_units.html", context)


@login_required
def lecturer_units_edit(request, pk):
    title = "Update Units"
    button = "Update Unit"
    queryset = LecturerUnits.objects.get(id=pk)
    form = LecturerUnitsForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = LecturerUnitsForm(request.POST or None, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Unit Updated Successfully")
            return HttpResponseRedirect("/school/lecturer_units")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "next/lecturer_units.html", context)


@login_required
def lecturer_units_delete(request, pk):
    title = "Delete Unit"
    button = "Delete Unit"
    queryset = LecturerUnits.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Unit Deleted From My List")
        return HttpResponseRedirect("/school/lecturer_units")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def ListAllLecturerUnits(request):
    title = "List Of All Lecturers' Units"
    queryset = LecturerUnits.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/lecturer_unit_list.html", context)

# =================================================================================
# Seats


@login_required
def seats(request):
    title = "Add New Seats/Positions For Students To Vie"
    button = "Add Seat"
    form = SeatsForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Seat/Position Added Successfully")
        return HttpResponseRedirect("/school/list_seats")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "next/add-edit-seats.html", context)


@login_required
def seats_edit(request, pk):
    title = "Edit Existing Seats/Positions For Students To Vie"
    button = "Add Seat"
    queryset = Seats.objects.get(id=pk)
    form = SeatsForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = SeatsForm(request.POST or None, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Seat/Position Updated Successfully")
            return HttpResponseRedirect("/school/list_seats")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "next/add-edit-seats.html", context)


@login_required
def seats_delete(request, pk):
    title = "Delete Seat"
    button = "Delete Seat"
    queryset = Seats.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Seat/Position Deleted From Database")
        return HttpResponseRedirect("/school/list_seats")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_seats(request):
    title = "List Of All Positions/Seats"
    queryset = Seats.objects.all()
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/list_seats.html", context)
# ==========================================================================================
# Notice Board


@login_required
def add_notice(request):
    title = "Add Notice"
    button = "Add Notice"
    form = NoticeBoardForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.written_by = request.user
        instance.full_name = request.user.first_name + \
            ' '+str(request.user.last_name)
        instance.stage = form.cleaned_data['stage']
        instance.notice = form.cleaned_data['notice']
        instance.signature = form.cleaned_data['signature']
        instance.save()
        messages.success(request, "Notice Added Successfully on Board")
        return HttpResponseRedirect("/school/add_notice")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "next/add_notice.html", context)


@login_required
def delete_notice(request, pk):
    title = "Delete Notice"
    button = "Delete Notice"
    queryset = NoticeBoard.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Notice Deleted From Board")
        return HttpResponseRedirect("/school/list_notices")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_notices(request):
    title = "School Notice Board"
    queryset = NoticeBoard.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/list_notices.html", context)
# =================================================================================================
# Voting


@login_required
def register_polititian(request):
    title = "Register Politician"
    button = "Register"
    form = VotingForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.written_by = request.user
        instance.full_name = request.user.first_name + \
            ' '+str(request.user.last_name)
        instance.stage = form.cleaned_data['stage']
        instance.notice = form.cleaned_data['notice']
        instance.signature = form.cleaned_data['signature']
        instance.save()
        messages.success(request, "Polititian Registerd Successfully")
        return HttpResponseRedirect("/school/register_polititian")
    context = {
        "title": title,
        "form": form,
        "button": button
    }
    return render(request, "next/register_polititian.html", context)


@login_required
def edit_polititian(request, pk):
    title = "Edit Politician"
    button = "Register"
    queryset = Voting.objects.get(id=pk)
    form = VotingForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        form = VotingForm(request.POST or None, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Polititian Updated Successfully")
            return HttpResponseRedirect("/school/list_politicians")
    context = {
        "title": title,
        "form": form,
        "button": button
    }
    return render(request, "next/register_polititian.html", context)


@login_required
def delete_polititian(request, pk):
    title = "Delete Politician"
    button = "Delete"
    queryset = Voting.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Polititian Deleted from Database")
        return HttpResponseRedirect("/school/list_politicians")
    context = {
        "title": title,
        "form": form,
        "button": button
    }
    return render(request, "school/delete_items.html", context)


def list_politicians(request):
    title = "List Of All Polititians"
    queryset = Voting.objects.all()
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/list_polititians.html", context)

# =============================================================================================
# Suggestions


@login_required
def add_suggestion(request):
    title = "Add Suggestion"
    button = "Add"
    form = SuggestionBoxForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.written_by = request.user
        instance.full_name = request.user.first_name + \
            ' '+str(request.user.last_name)
        instance.suggestion = form.cleaned_data['suggestion']
        instance.save()
        messages.success(request, "Suggestion Sent Successfully")
        return HttpResponseRedirect("/school/add_suggestion")
    context = {
        "title": title,
        "form": form,
        "button": button
    }
    return render(request, "next/send_suggestion.html", context)


@login_required
def delete_suggestion(request, pk):
    title = "Delete Suggestion"
    button = "Delete"
    queryset = SuggestionBox.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Suggestion Deleted from Database")
        return HttpResponseRedirect("/school/list_suggestions")
    context = {
        "title": title,
        "button": button
    }
    return render(request, "school/delete_items.html", context)


def list_suggestions(request):
    title = "List Of All Suggestions"
    queryset = SuggestionBox.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/list_suggestions.html", context)

def send_notice(request):
    title="Compose New Notice And Send"
    form=NoticeBoardForm(request.POST or None)
    if form.is_valid():
        full_name=request.user.first_name+" "+request.user.middle_name+" "+request.user.last_name
        written_by=request.user
        group=form.cleaned_data['group']
        signature=form.cleaned_data['signature']
        notice=form.cleaned_data['notice']
        reg=NoticeBoard(full_name=full_name, written_by=written_by,group=group,signature=signature, notice=notice)
        reg.save()
        messages.success(request, "Notice Published Successfully on the Notice Board")
        return redirect("/")
    context={
        "form":form,
        "title":title
    }
    return render(request, "notifications/compose_notice.html", context)

def edit_notice(request, pk):
    title="Edit Notice And Send"
    queryset=NoticeBoard.objects.get(id=pk)
    form=NoticeBoardForm(request.POST or None, queryset)
    if request.method=="POST":
        form=NoticeBoardForm(request.POST or None, queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Notice Updated Successfully on the Notice Board")
            return redirect("/")
    context={
        "form":form,
        "title":title
    }
    return render(request, "notifications/compose_notice.html", context)

def list_notices(request):
    title="ALL NOTICES"
    queryset=NoticeBoard.objects.all()
    context={
        "title":title,
        "queryset":queryset
    }
    return render(request, "notifications/all_public_notices.html", context)

def read_notices(request,pk):
    title="Read Notice"
    queryset=NoticeBoard.objects.get(id=pk)
    