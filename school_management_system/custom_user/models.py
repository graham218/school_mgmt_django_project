from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    first_name=models.CharField(max_length=255, blank=False, null=False, default="John")
    middle_name=models.CharField(max_length=255, blank=False, null=False, default="Doe")
    last_name=models.CharField(max_length=255, blank=False, null=False, default="Smith")
    profile_photo = models.ImageField(upload_to="profile_pics/", blank=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_non_staff = models.BooleanField(default=False)