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

admin.site.register(Address, AddressAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Programmes, ProgrammesAdmin)