from django.db import models
from django.views import View
from django.shortcuts import render
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    birthday=models.DateField(null=True, blank=True, default=datetime.date.today)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



class Signin(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Upload_cv(models.Model):
    RESIDENCY_CHOICES = [
        ('citizen', 'Citizen'),
        ('permanent_resident', 'Permanent Resident'),
        ('work_permit', 'Work Permit')
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    message = models.TextField(max_length=50)
    cv = models.FileField(upload_to='cv_files')
    cover_letter = models.FileField(upload_to='cover_letter_files')
    residency = models.CharField(max_length=20, choices=RESIDENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname


class Upload_resume(models.Model):
    email = models.EmailField(max_length=50, default='')
    resume_file = models.FileField(upload_to='upload_resume',null=True, blank=True)

    def get(self, request):
        return render(request, 'upload.html')
