from django.urls import path
from . import views  # Import the views module from the current directory

urlpatterns = [
    path('', views.login_view, name='login'),
]
