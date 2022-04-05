from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import *
import datetime

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
    context = {
        "school": school,
        "box": box,
        'tel':tel,
        'email':email,
        'date_downloaded':date_downloaded,
        'queryset':queryset
    }
    pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr1_pdf.html', context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'Year1-Exam-Card-%s.pdf'
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content
    return response


