from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customusers(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    profile_picture=models.ImageField(upload_to='profile_pics')
    address_line1=models.CharField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)