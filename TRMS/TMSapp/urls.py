from django.urls import path
from . import views  # Import the views module from the current directory

urlpatterns = [
    path('', views.home, name='home'),  # Maps the root URL to the home view
]
