from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class University(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='school_img/')
    website = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class School(models.Model):
    owner = models.ForeignKey(User)
    university = models.ForeignKey(University)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='school_img/')
    website = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now, null=True,blank=True)
    modified_at = models.DateTimeField(default=timezone.now, null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    Many_to_Many=True
    counrty_name=(
        ('IND','India'),
        ('AUS','Austrelia'),
        ('FND','Finland'),
        ('UK','United Kingdom'),
        ('GM','Germany'),
    )
    street_1 = models.CharField(max_length=30)
    street_2 = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=10, choices=counrty_name)
    zip_code = models.IntegerField(null=True,blank=True)
    mobile_no = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.city

class Student(models.Model):
    
    
    school = models.ForeignKey(School)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    roll_no = models.IntegerField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.CharField(max_length=20)
    address = models.ManyToManyField(Address,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    
        

    def __str__(self):
        return self.first_name




