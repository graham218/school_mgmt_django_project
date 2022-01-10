from django.contrib import admin
from .models import *

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'locality', 'city', 'state')
    list_filter = ('city', 'state')
    list_per_page = 10
    search_fields = ('locality', 'city', 'state')

class FacultyAdmin(admin.ModelAdmin):
    list_display=('school','date_created','date_updated')
    list_filter=('school')
    search_fields=('school')

class ProgrammesAdmin(admin.ModelAdmin):
    list_display=('name','faculty')
    list_filter=('name','faculty')
    search_fields=('name')

class StagesAdmin(admin.ModelAdmin):
    list_display=('year')
    list_filter=('year')
    search_fields=('year')

class GenderAdmin(admin.ModelAdmin):
    list_display=('gender')
    list_filter=('gender')
    search_fields=('gender')

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'admission_no', 'full_name', 'nationality',
     'gender', 'national_ID_number', 'birth_cert_no', 'phone_number',
     'DOB', 'date_of_admission', 'date_of_graduation', 'programme',
     'stage', 'postal_address', 'school_email', 'school_email_password',
     'total_fees_billed', 'total_fees_paid', 'balance')
    list_filter = ('user', 'full_name', 'admission_no')
    list_per_page = 10
    search_fields = ('admission_no', 'user', 'full_name')


admin.site.register(Address, AddressAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Programmes, ProgrammesAdmin)
admin.site.register(Stages, StagesAdmin)
admin.site.register(Gender, GenderAdmin)