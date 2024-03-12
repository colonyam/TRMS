from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Check if the user has admin access
                    if user.is_staff or user.is_superuser:
                        # Redirect the user to the Django admin dashboard
                        return redirect('/admin/')
                    else:
                        # Redirect to a different page for non-admin users
                        return redirect('home')
                else:
                    # Account is inactive, add an error message
                    messages.error(request, 'Your account is inactive.')
            else:
                # Authentication failed, add an error message
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
