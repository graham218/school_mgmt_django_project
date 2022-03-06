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
def FeeReceiptList(request):
    title = 'List All Fee Student Receipts'
    queryset = FeeReceipt.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "next/fee_receipt_list.html", context)

@login_required
def my_reg_units_year_page(request):
    title="Choose Your Year Of Study"
    context={
        "title":title
    }
    return render(request, "units/my_reg_units_year_page.html", context)

@login_required
def list_marks_year_page(request):
    title="Choose Your Year Of Study"
    context={
        "title":title
    }
    return render(request, "units/pages/list_marks_year_page.html", context)
# ------------------------------------------------------------------------------------
# Resits/Retakes
@login_required
def my_resit_year_page(request):
    title="Choose Your Year Of Study To Register Resits/Retakes/Special Exams"
    context={
        "title":title
    }
    return render(request, "units/pages/my_resit_year_page.html", context)

@login_required
def list_resit_year_page(request):
    title="Choose Year Of Study To Enter Marks And Grades"
    context={
        "title":title
    }
    return render(request, "units/pages/list_resit_year_page.html", context)
# ----------------------------------------------------------------------------------------
# Year 1 Resits/Retakes
@login_required
def resit_reg_year1(request):
    title = "Resit/Retake Registration Year 1"
    button="Register Resit"
    form = ResitRegYr1Form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Resit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr1/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_retakes.html", context)


@login_required
def unregister_resit_yr1(request, pk):
    queryset = resit_exam_yr1.objects.get(id=pk)
    title = "Unregister Resit/Retake"
    button="Unregister Resit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Resit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr1")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_registered_resits1(request):
    title = 'List of Registered Students Doing Resits/Retakes'
    queryset = resit_exam_yr1.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_resits/list_registered_resits_yr1.html", context)

def my_registered_resits_yr1(request):
    title = 'MY REGISTERED RESITS OF YEAR 1'
    queryset = resit_exam_yr1.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_resits/my_registered_resits_yr1.html", context)
# End of yr 1 retakes

# Year 2 Resits/Retakes
@login_required
def resit_reg_year2(request):
    title = "Resit/Retake Registration Year 2"
    button="Register Resit"
    form = ResitRegYr2Form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Resit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr2/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_retakes.html", context)


@login_required
def unregister_resit_yr2(request, pk):
    queryset = resit_exam_yr2.objects.get(id=pk)
    title = "Unregister Resit/Retake"
    button="Unregister Resit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Resit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr2")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_registered_resits2(request):
    title = 'List of Registered Students Doing Resits/Retakes Year 2'
    queryset = resit_exam_yr2.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_resits/list_registered_resits_yr2.html", context)

def my_registered_resits_yr2(request):
    title = 'MY REGISTERED RESITS OF YEAR 2'
    queryset = resit_exam_yr2.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_resits/my_registered_resits_yr2.html", context)
# End Of Yr 2 Retakes

# Year 3 Resits/Retakes
@login_required
def resit_reg_year3(request):
    title = "Resit/Retake Registration Year 3"
    button="Register Resit"
    form = ResitRegYr3Form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Resit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr3/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_retakes.html", context)


@login_required
def unregister_resit_yr3(request, pk):
    queryset = resit_exam_yr3.objects.get(id=pk)
    title = "Unregister Resit/Retake"
    button="Unregister Resit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Resit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr3")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_registered_resits3(request):
    title = 'List of Registered Students Doing Resits/Retakes'
    queryset = resit_exam_yr3.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_resits/list_registered_resits_yr3.html", context)

def my_registered_resits_yr3(request):
    title = 'MY REGISTERED RESITS OF YEAR 3'
    queryset = resit_exam_yr3.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_resits/my_registered_resits_yr3.html", context)
# End of yr 3 Retakes

# Year 4 Resits/Retakes
@login_required
def resit_reg_year4(request):
    title = "Resit/Retake Registration Year 4"
    button="Register Resit"
    form = ResitRegYr4Form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Resit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr4/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_retakes.html", context)


@login_required
def unregister_resit_yr4(request, pk):
    queryset = resit_exam_yr4.objects.get(id=pk)
    title = "Unregister Resit/Retake"
    button="Unregister Resit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Resit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr4")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_registered_resits4(request):
    title = 'List of Registered Students Doing Resits/Retakes'
    queryset = resit_exam_yr4.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_resits/list_registered_resits_yr4.html", context)

def my_registered_resits_yr4(request):
    title = 'MY REGISTERED RESITS OF YEAR 4'
    queryset = resit_exam_yr4.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_resits/my_registered_resits_yr4.html", context)
# End Of Yr 4 Retakes

# Year 5 Resits/Retakes
@login_required
def resit_reg_year5(request):
    title = "Resit/Retake Registration Year 5"
    button="Register Resit"
    form = ResitRegYr5Form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Resit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr5/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_retakes.html", context)


@login_required
def unregister_resit_yr5(request, pk):
    queryset = resit_exam_yr5.objects.get(id=pk)
    title = "Unregister Resit/Retake"
    button="Unregister Resit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Resit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr5")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_registered_resits5(request):
    title = 'List of Registered Students Doing Resits/Retakes'
    queryset = resit_exam_yr5.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_resits/list_registered_resits_yr5.html", context)

def my_registered_resits_yr5(request):
    title = 'MY REGISTERED RESITS OF YEAR 5'
    queryset = resit_exam_yr5.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_resits/my_registered_resits_yr5.html", context)
# End of yr 5 retakes

# Year 6 Resits/Retakes
@login_required
def resit_reg_year6(request):
    title = "Resit/Retake Registration Year 6"
    button="Register Resit"
    form = ResitRegYr6Form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Resit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr6/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_retakes.html", context)


@login_required
def unregister_resit_yr6(request, pk):
    queryset = resit_exam_yr6.objects.get(id=pk)
    title = "Unregister Resit/Retake"
    button="Unregister Resit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Resit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr6")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_registered_resits6(request):
    title = 'List of Registered Students Doing Resits/Retakes'
    queryset = resit_exam_yr6.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_resits/list_registered_resits_yr6.html", context)

def my_registered_resits_yr6(request):
    title = 'MY REGISTERED RESITS OF YEAR 6'
    queryset = resit_exam_yr6.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_resits/my_registered_resits_yr6.html", context)
# End of yr 6 retakes

# Year 7 Resits/Retakes
@login_required
def resit_reg_year7(request):
    title = "Resit/Retake Registration Year 7"
    button="Register Resit"
    form = ResitRegYr7Form(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.full_name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
        instance.stage=form.cleaned_data['stage']
        instance.unit_name=form.cleaned_data['unit_name']
        instance.save()
        messages.success(request, "Resit Registered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr7/")
    context = {
        "title": title,
        "form": form,
        "button": button,
    }
    return render(request, "units/register_retakes.html", context)


@login_required
def unregister_resit_yr7(request, pk):
    queryset = resit_exam_yr7.objects.get(id=pk)
    title = "Unregister Resit/Retake"
    button="Unregister Resit"
    if request.method == "POST":
        queryset.delete()
        messages.error(request, "Resit Unregistered Successfully")
        return HttpResponseRedirect("/school/my_registered_resits_yr7")
    context = {
        "title": title,
        "button": button,
    }
    return render(request, "school/delete_items.html", context)


def list_registered_resits7(request):
    title = 'List of Registered Students Doing Resits/Retakes'
    queryset = resit_exam_yr7.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/list_registered_resits/list_registered_resits_yr7.html", context)

def my_registered_resits_yr7(request):
    title = 'MY REGISTERED RESITS OF YEAR 7'
    queryset = resit_exam_yr7.objects.filter(user=request.user)
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "units/my_registered_resits/my_registered_resits_yr7.html", context)
# End of yr 7 retakes
# End Of Resits/Retakes
# ---------------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------------------------
# Noticeboard
@login_required
def send_notice(request):
    title="Compose New Notice And Send"
    form=NoticeBoardForm(request.POST or None)
    if form.is_valid():
        full_name=request.user.first_name+" "+request.user.middle_name+" "+request.user.last_name
        written_by=request.user
        group=form.cleaned_data['group']
        signature=form.cleaned_data['signature']
        notice=form.cleaned_data['notice']
        notice_title=form.cleaned_data['notice_title']
        reg=NoticeBoard(full_name=full_name, written_by=written_by,group=group,signature=signature, notice=notice, notice_title=notice_title)
        reg.save()
        messages.success(request, "Notice Published Successfully on the Notice Board")
        return redirect("/school/all_public_notices")
    context={
        "form":form,
        "title":title
    }
    return render(request, "notifications/compose_notice.html", context)

@login_required
def edit_notice(request, pk):
    title="Edit Notice And Send"
    queryset=NoticeBoard.objects.get(id=pk)
    form=NoticeBoardForm(request.POST or None, queryset)
    if request.method=="POST":
        form=NoticeBoardForm(request.POST or None, queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Notice Updated Successfully on the Notice Board")
            return redirect("/school/all_public_notices")
    context={
        "form":form,
        "title":title
    }
    return render(request, "notifications/compose_notice.html", context)

@login_required
def list_notices(request):
    title="ALL NOTICES"
    queryset=NoticeBoard.objects.all()
    context={
        "title":title,
        "queryset":queryset
    }
    return render(request, "notifications/all_public_notices.html", context)

@login_required
def read_notices(request,pk):
    title="Read Notice"
    queryset=NoticeBoard.objects.get(id=pk)
    context={
        "title":title,
        "queryset":queryset
    }
    return render(request, "notifications/read_public_notices.html", context)

def delete_notice(request, pk):
    queryset=NoticeBoard.objects.get(id=pk)
    title="Delete Notice"
    if request.method=="POST":
        queryset.delete()
        messages.error(request, "Notice "+str(queryset.notice_title)+" Has Been deleted from the Notice Board!!!!!")
        return redirect("/school/all_public_notices")
    context={
        "title":title
    }
    return render(request, "notifications/delete_notices.html", context)

# End of Noticeboard
# --------------------------------------------------------------------------------------------