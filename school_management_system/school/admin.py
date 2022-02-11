from django.contrib import admin
from .models import *

# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['school', 'date_created', 'date_updated']
    list_filter = ['school']
    search_fields = ['school']


class ProgrammesAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty']
    list_filter = ['name', 'faculty']
    search_fields = ['name']

class GenderAdmin(admin.ModelAdmin):
    list_display = ['gender']
    list_filter = ['gender']
    search_fields = ['gender']


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'admission_no', 'full_name', 'nationality',
                    'stud_gender', 'national_ID_number', 'birth_cert_no', 'phone_number',
                    'DOB', 'date_of_admission', 'date_of_graduation', 'programme',
                    'stage', 'postal_address', 'school_email', 'school_email_password',
                    'total_fees_billed', 'total_fees_paid', 'balance']
    list_filter = ['user', 'full_name', 'admission_no']
    list_per_page = 10
    search_fields = ['admission_no', 'user', 'full_name']


class UnitsAdmin(admin.ModelAdmin):
    list_display = ['unit_name', 'date_created', 'date_updated']
    list_filter = ['unit_name']
    search_fields = ['unit_name']


class LectureAdmin(admin.ModelAdmin):
    list_display = ['user', 'lec_no', 'full_name', 'nationality',
                    'lec_gender', 'national_ID_number', 'phone_number',
                    'DOB', 'postal_address', 'school_email', 'school_email_password',
                    'total_salary_billed', 'total_salary_paid', 'balance']
    list_filter = ['user', 'full_name', 'lec_no']
    list_per_page = 10
    search_fields = ['user', 'full_name', 'lec_no']


class MarksAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage', 'unit_or_subject_name',
                    'marks', 'grade', 'date_created', 'date_updated']
    list_per_page = 10
    search_fields = ['user', 'full_name', 'unit_or_subject_name', 'stage']
    list_filter = ['user', 'full_name', 'unit_or_subject_name', 'stage']


class MarksAdmin2(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage', 'unit_or_subject_name',
                    'marks', 'grade', 'date_created', 'date_updated']
    list_per_page = 10
    search_fields = ['user', 'full_name', 'unit_or_subject_name', 'stage']
    list_filter = ['user', 'full_name', 'unit_or_subject_name', 'stage']


class MarksAdmin3(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage', 'unit_or_subject_name',
                    'marks', 'grade', 'date_created', 'date_updated']
    list_per_page = 10
    search_fields = ['user', 'full_name', 'unit_or_subject_name', 'stage']
    list_filter = ['user', 'full_name', 'unit_or_subject_name', 'stage']


class MarksAdmin4(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage', 'unit_or_subject_name',
                    'marks', 'grade', 'date_created', 'date_updated']
    list_per_page = 10
    search_fields = ['user', 'full_name', 'unit_or_subject_name', 'stage']
    list_filter = ['user', 'full_name', 'unit_or_subject_name', 'stage']


class MarksAdmin5(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage', 'unit_or_subject_name',
                    'marks', 'grade', 'date_created', 'date_updated']
    list_per_page = 10
    search_fields = ['user', 'full_name', 'unit_or_subject_name', 'stage']
    list_filter = ['user', 'full_name', 'unit_or_subject_name', 'stage']


class MarksAdmin6(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage', 'unit_or_subject_name',
                    'marks', 'grade', 'date_created', 'date_updated']
    list_per_page = 10
    search_fields = ['user', 'full_name', 'unit_or_subject_name', 'stage']
    list_filter = ['user', 'full_name', 'unit_or_subject_name', 'stage']


class MarksAdmin7(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage', 'unit_or_subject_name',
                    'marks', 'grade', 'date_created', 'date_updated']
    list_per_page = 10
    search_fields = ['user', 'full_name', 'unit_or_subject_name', 'stage']
    list_filter = ['user', 'full_name', 'unit_or_subject_name', 'stage']


class fee_payment_admin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'amount_paid',
                    'payment_method', 'date_paid', 'date_paid']
    list_per_page = 10


class FeeReceiptAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage',
                    'exams', 'co_ocurricular_activities', 'hostel_charges', 'library_charges',
                    'internet_charges', 'electricity_charges', 'food_charges', 'furniture_charges',
                    'water_charges', 'date_updated']
    list_per_page = 10
    search_fields=['user', 'full_name', 'stage']
    list_filter=['user', 'full_name', 'stage']

class SpecialExamAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'stage',
                    'unit_name', 'marks', 'grade', 'comments', 'date_updated']
    list_per_page = 10
    search_fields=['user', 'full_name', 'stage']
    list_filter=['user', 'full_name', 'stage']

class LecturerUnitsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'unit_name',
                    'level_of_understanding', 'created_at']
    list_per_page = 10
    search_fields = ['full_name', 'unit_name']
    list_filter = ['full_name', 'unit_name']

class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ['written_by', 'full_name', 'notice', 'signature']
    list_per_page = 10
    search_fields = ['written_by', 'full_name', 'notice', 'signature']
    list_filter = ['written_by', 'full_name', 'notice', 'signature']
class VotingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'stage', 'course', 'seat',
                    'votes', 'position', 'status', 'created_at', 'updated_at']
    list_per_page = 10
    search_fields = ['full_name', 'stage', 'course', 'seat']
    list_filter = ['full_name', 'stage', 'course', 'seat']

class SuggestionBoxAdmin(admin.ModelAdmin):
    list_display = ['written_by', 'full_name', 'suggestion', 'check',
                    'status', 'created_at', 'updated_at']
    list_per_page = 10
    search_fields = ['written_by', 'full_name', 'suggestion', 'check']
    list_filter = ['written_by', 'full_name', 'suggestion', 'check']

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Programmes, ProgrammesAdmin)
admin.site.register(Stages)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Units, UnitsAdmin)
admin.site.register(Lectures, LectureAdmin)
admin.site.register(marks_yr1, MarksAdmin)
admin.site.register(marks_yr2, MarksAdmin2)
admin.site.register(marks_yr3, MarksAdmin3)
admin.site.register(marks_yr4, MarksAdmin4)
admin.site.register(marks_yr5, MarksAdmin5)
admin.site.register(marks_yr6, MarksAdmin6)
admin.site.register(marks_yr7, MarksAdmin7)
admin.site.register(fee_payment, fee_payment_admin)
admin.site.register(FeeReceipt, FeeReceiptAdmin)
admin.site.register(SpecialExam, SpecialExamAdmin)
admin.site.register(LecturerUnits, LecturerUnitsAdmin)
admin.site.register(NoticeBoard, NoticeBoardAdmin)
admin.site.register(Voting, VotingAdmin)
admin.site.register(SuggestionBox, SuggestionBoxAdmin)