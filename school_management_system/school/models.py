from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
User=get_user_model()


# Create your models here.

# Create your models here.

class Faculty(models.Model):
    school = models.CharField(max_length=255, blank=False, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.school


class Programmes(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Stages(models.Model):
    year = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.year



class Gender(models.Model):
    gender = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.gender


class Students(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE)
    admission_no = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    stud_gender = models.ForeignKey(
        Gender, on_delete=models.CASCADE, blank=False)
    national_ID_number = models.CharField(
        max_length=255, blank=True, null=True)
    birth_cert_no = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    DOB = models.DateField()
    date_of_admission = models.DateField(blank=True, null=True)
    date_of_graduation = models.DateField(blank=True, null=True)
    programme = models.ForeignKey(
        Programmes, on_delete=models.CASCADE, max_length=255, blank=True)
    stage = models.ForeignKey(
        Stages, on_delete=models.CASCADE, blank=False, null=True)
    # profile_photo = models.ImageField(
    #     upload_to="students_pic/", blank=False, null=True)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    school_email = models.EmailField(max_length=255, blank=True, null=True)
    school_email_password = models.CharField(
        max_length=255, blank=True, null=True)
    total_fees_billed = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    total_fees_paid = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.full_name


class Units(models.Model):
    unit_name = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.unit_name


class Lectures(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE)
    lec_no = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True)
    lec_gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    national_ID_number = models.CharField(
        max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True)
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    # profile_photo = models.ImageField(upload_to="lecturer_pic/", blank=True)
    postal_address = models.CharField(max_length=255, blank=True)
    school_email = models.EmailField(max_length=255, blank=True)
    school_email_password = models.CharField(max_length=255, blank=True)
    total_salary_billed = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name


# ---------------------------------------------------------------------------------------
# Normal Exams
class marks_yr1(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=False)
    unit_or_subject_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=False)
    marks = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.unit_or_subject_name

class marks_yr2(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=False)
    unit_or_subject_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=False)
    marks = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.unit_or_subject_name


class marks_yr3(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=False)
    unit_or_subject_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=False)
    marks = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.unit_or_subject_name

class marks_yr4(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=False)
    unit_or_subject_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=False)
    marks = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.unit_or_subject_name

class marks_yr5(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=False)
    unit_or_subject_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=False)
    marks = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.unit_or_subject_name

class marks_yr6(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=False)
    unit_or_subject_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=False)
    marks = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.unit_or_subject_name

class marks_yr7(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=False)
    unit_or_subject_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=False)
    marks = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.unit_or_subject_name

# End of normal Exams
# --------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
# Resit Exams
class resit_exam_yr1(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    date_registered = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

class resit_exam_yr2(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    date_registered = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

class resit_exam_yr3(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    date_registered = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

class resit_exam_yr4(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    date_registered = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

class resit_exam_yr5(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    date_registered = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

class resit_exam_yr6(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    date_registered = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

class resit_exam_yr7(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    date_registered = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

# End of Resit exams
# ---------------------------------------------------------------------------------------

class fee_payment(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    amount_paid=models.CharField(max_length=255, blank=True, null=True)
    payment_method=models.CharField(max_length=255, blank=True, null=True)
    paid=models.BooleanField(default=False)
    bill_reference_no=models.CharField(max_length=255, blank=True, null=True)
    phone_number=models.CharField(max_length=255, blank=True, null=True)
    date_paid = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

class salary_payment(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    amount_paid=models.CharField(max_length=255, blank=True, null=True)
    payment_method=models.CharField(max_length=255, blank=True, null=True)
    paid=models.BooleanField(default=False)
    bill_reference_no=models.CharField(max_length=255, blank=True, null=True)
    phone_number=models.CharField(max_length=255, blank=True, null=True)
    date_paid = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)


class FeeStructure(models.Model):
    program=models.ForeignKey(Programmes, max_length=255, on_delete=models.CASCADE, blank=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    exams = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    co_ocurricular_activities = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    hostel_charges = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    library_charges = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    internet_charges = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    electricity_charges = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    food_charges = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    furniture_charges = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    water_charges = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

    @property
    def total(self):
        total_school_fee=self.exams+self.co_ocurricular_activities+self.hostel_charges+self.library_charges+self.internet_charges+self.electricity_charges+self.food_charges+self.furniture_charges+self.water_charges


class SpecialExam(models.Model):
    user = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage=models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    marks = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    date_registered = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, auto_now=True)

class LecturerUnits(models.Model):
    username = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255,blank=True)
    unit_name = models.ForeignKey(Units, max_length=255, on_delete=models.CASCADE, blank=True)
    level_of_understanding = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(
        null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

NOTICE_CATEGORY=[
    ('PUBLIC','PUBLIC'),
    ('STAFF','STAFF'),
    ('SUPPLIERS','SUPPLIERS'),
    ('STUDENTS','STUDENTS'),
    ('LECTURERS','LECTURERS')
]
class NoticeBoard(models.Model):
    written_by = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    group=models.CharField(max_length=255, blank=False, choices=NOTICE_CATEGORY, default="PUBLIC")
    notice_title=models.CharField(max_length=255, blank=True, null=True)
    notice = RichTextUploadingField(default="")
    signature = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(
        null=True, blank=True, auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

class Seats(models.Model):
    seat=models.CharField(max_length=255, blank=True, null=False)
    def __str__(self):
        return self.seat

class Voting(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    stage = models.ForeignKey(Stages, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    course = models.ForeignKey(Programmes, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    seat = models.ForeignKey(Seats, max_length=255, on_delete=models.CASCADE, blank=True, default="")
    votes = models.CharField(max_length=5000, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(
        null=True, blank=True, auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)

class SuggestionBox(models.Model):
    written_by = models.ForeignKey(User, max_length=255, on_delete=models.CASCADE, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    suggestion = RichTextUploadingField(default='')
    check=models.BooleanField(default=False, blank=True)
    status=models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(
        null=True, blank=True, auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)