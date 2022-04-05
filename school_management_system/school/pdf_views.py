from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Automaticly downloads to PDF file
class exam_card_yr1_pdf(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('pdf_export/exam/exam_card/exam_card_yr1_pdf.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Year1-Exam-Card-%s.pdf" %("1234567890")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response