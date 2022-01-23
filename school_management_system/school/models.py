from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User",
                             on_delete=models.CASCADE)
    locality = models.CharField(
        max_length=150, verbose_name="Nearest Location")
    city = models.CharField(max_length=150, verbose_name="City")
    state = models.CharField(max_length=150, verbose_name="State")

    def __str__(self):
        return self.locality


class Faculty(models.Model):
    school = models.CharField(max_length=255, blank=True, null=True)
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
    profile_photo = models.ImageField(
        upload_to="students_pic/", blank=False, null=True)
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
    profile_photo = models.ImageField(upload_to="lecturer_pic/", blank=True)
    postal_address = models.CharField(max_length=255, blank=True)
    school_email = models.EmailField(max_length=255, blank=True)
    school_email_password = models.CharField(max_length=255, blank=True)
    total_salary_billed = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name


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
