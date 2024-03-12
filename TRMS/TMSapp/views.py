from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_active:
                login(request, user)
                
                # Direct TMS Administrators to the Django admin site
                if user.is_staff or user.groups.filter(name='TMS Administrator').exists():
                    return redirect('/admin/')
                
                # Redirect based on group membership for other users
                elif user.groups.filter(name='Manager').exists():
                    return redirect('manager_dashboard')  # Redirect to Manager dashboard
                elif user.groups.filter(name='Driver').exists():
                    return redirect('driver_dashboard')  # Redirect to Driver dashboard
                else:
                    messages.error(request, 'No role assigned. Please contact the administrator.')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Dashboard views for each user type
@login_required
def tms_admin_dashboard(request):
    # Ensure the user is a TMS Administrator
    if not request.user.is_staff:
        messages.error(request, "You don't have permission to access this page.")
        return redirect('login')
    return render(request, '/admin/')

@login_required
def manager_dashboard(request):
    # Ensure the user is a Manager
    if not request.user.groups.filter(name='Manager').exists():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('login')
    return render(request, 'manager_dashboard.html')

@login_required
def driver_dashboard(request):
    # Ensure the user is a Driver
    if not request.user.groups.filter(name='Driver').exists():
        messages.error(request, "You don't have permission to access this page.")
        return redirect('login')
    return render(request, 'driver_dashboard.html')
