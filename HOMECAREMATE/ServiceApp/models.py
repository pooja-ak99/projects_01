from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='category/cover',null=True,blank=True)
    our_services = models.TextField()

    def pointlist(self):
        return self.our_services.split('\n')

    def __str__(self):
        return self.category_name


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, default="")
    address = models.TextField()

    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_serviceprovider = models.BooleanField(default=False)


class Career(models.Model):
    fullname = models.CharField(max_length=60)
    dob = models.DateField()
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()
    qualification = models.CharField(max_length=50)
    skills = models.TextField()
    location = models.CharField(max_length=100)
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Other'),
    ]
    service = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    STATUS_SELECTED = 'selected'
    STATUS_REJECTED = 'rejected'
    STATUS_PENDING = 'pending'
    STATUS_CHOICES = [
        (STATUS_SELECTED, 'Selected'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_PENDING, 'Pending'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    resume = models.FileField(upload_to='career/resume')
    id_proof = models.FileField(upload_to='career/id_proof')
    profile_photo = models.ImageField(upload_to='career/propic', null=True, blank=True)

    def __str__(self):
        return self.fullname


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    service = models.ForeignKey(Category, on_delete=models.CASCADE)
    service_date = models.DateField()
    special_request = models.TextField()

    def __str__(self):
        return self.name














