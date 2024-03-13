from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

default_image_path = settings.STATIC_URL + 'assets/img/faces/avatar.jpg'


class Driver(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    licence_number = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    car_in_charge_of = models.CharField(max_length=100)
    company_from = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default = 'Okeyo Mercy(Default)',max_length=100, null =True)
    bio = models.TextField(default= 'i am mercy achieng i am a transcountry driver with 4years of experience',blank=True)
    profile_image = models.ImageField(upload_to='C:\\Users\\user\\Desktop\\TRMS\\TRMS\\TRMS\\static\\assets\\img', blank=True,default='static/assets/img/faces/avatar.jpg')

    def __str__(self):
        return "{self.user.username} 's profile"