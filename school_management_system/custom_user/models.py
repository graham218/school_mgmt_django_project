from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="profile_pics/", blank=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_non_staff = models.BooleanField(default=False)