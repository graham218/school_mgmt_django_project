from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import *
import datetime
from django.contrib.auth.decorators import login_required


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Automaticly downloads to PDF file

def exam_card_yr1_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr1.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr1_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-1-Exam-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def exam_card_yr2_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr2.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr2_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-2-Exam-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def exam_card_yr3_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr3.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr3_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-3-Exam-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def exam_card_yr4_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr4.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr4_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-4-Exam-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def exam_card_yr5_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr5.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr5_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-5-Exam-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def exam_card_yr6_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr6.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr6_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-6-Exam-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def exam_card_yr7_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr7.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr7_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-7-Exam-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


# Download Resit card pdf

def resit_card_yr1_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = resit_exam_yr1.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/retakes/resit_card/resit_card_yr1_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-1-Retake-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def resit_card_yr2_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = resit_exam_yr2.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/retakes/resit_card/resit_card_yr2_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-2-Retake-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def resit_card_yr3_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = resit_exam_yr3.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/retakes/resit_card/resit_card_yr3_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-3-Retake-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def resit_card_yr4_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = resit_exam_yr4.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/retakes/resit_card/resit_card_yr4_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-4-Retake-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def resit_card_yr5_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = resit_exam_yr5.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/retakes/resit_card/resit_card_yr5_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-5-Retake-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def resit_card_yr6_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = resit_exam_yr6.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/retakes/resit_card/resit_card_yr6_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-6-Retake-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


def resit_card_yr7_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = resit_exam_yr7.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/retakes/resit_card/resit_card_yr7_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-7-Retake-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


# Download results slip/card
def results_slip_year1_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr1.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-1-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response

def results_slip_year2_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr2.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-2-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response

def results_slip_year3_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr3.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-3-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response

def results_slip_year4_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr4.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-4-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response

def results_slip_year5_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr5.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-5-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response

def results_slip_year6_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr6.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-6-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response

def results_slip_year7_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr7.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-7-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


# Fee payment receipt
def results_slip_year7_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr7.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-7-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


# Salary Payment receipt
def results_slip_year7_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr7.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-7-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


# Fee Structure
def results_slip_year7_pdf(request):
    school = 'GRAHAM UNIVERSITY OF INNOVATION AND TECHNOLOGY'
    box='P.O BOX 7676 NAIROBI(K)'
    tel='+254-787675655768'
    email='grahambill011@gmail.com'
    date_downloaded=datetime.datetime.now()
    queryset = marks_yr7.objects.filter(user=request.user)
    name=request.user.first_name+' '+str(request.user.middle_name)+' '+str(request.user.last_name)
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset,
        'full_name':name
    }
    pdf = render_to_pdf('pdf_export/exam/exam_results/exam_results_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year-7-Results-Card.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response

