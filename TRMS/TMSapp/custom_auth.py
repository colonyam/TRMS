# custom_auth.py

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from .models import Driver

class DriverAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            driver = Driver.objects.get(username=username, licence_number=password)
            return driver.user  # Assuming you have a ForeignKey to the User model in your Driver model
        except Driver.DoesNotExist:
            return None
