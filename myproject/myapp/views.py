from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        password = request.POST['password']

        # Create user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Authenticate and login the user
        user = authenticate(username=username, password=password)
        login(request, user)
        
        # Redirect to a success page
        return redirect('home')  # Replace 'success_page' with your desired redirect

    return render(request, 'register.html')  # Render your registration template

# Create your views here.
