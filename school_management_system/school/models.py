from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    locality = models.CharField(max_length=150, verbose_name="Nearest Location")
    city = models.CharField(max_length=150, verbose_name="City")
    state = models.CharField(max_length=150, verbose_name="State")

    def __str__(self):
        return self.locality

class Programmes(models.Model):
    name=models.CharField(max_length=255, blank=False)
    department=models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

class Students(models.Model):
    user=models.ForeignKey(User, max_length=255, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=255, blank=False)
    nationality=models.CharField(max_length=255, blank=True)
    national_ID_number=models.CharField(max_length=255, blank=True)
    birth_cert_no=models.CharField(max_length=255, blank=True)
    phone_number=models.CharField(max_length=255, blank=True)
    DOB=models.DateField(auto_now=False, auto_now_add=False)
    date_of_admission=models.DateTimeField(auto_now_add=False, auto_now=False)
    date_of_graduation=models.DateTimeField(auto_now_add=False, auto_now=False)
    programme=models.ForeignKey(Programmes, on_delete=models.CASCADE, max_length=255)
    #profile_photo=models.ImageField(upload_to="students_pic", blank=True )
    total_fees_billed=models.DecimalField(max_digits=10, decimal_places=2)
    total_fees_paid=models.DecimalField(max_digits=10, decimal_places=2)
    balance=models.DecimalField(max_digits=10, decimal_places=2)