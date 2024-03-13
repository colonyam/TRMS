from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Driver
from .forms import DriverForm
from django.contrib.auth.models import User

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
def driver (request):
    objects = Driver.objects.all()
    return render (request,'driver.html', {'drivers':driver})
def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'driver_list.html', {'drivers': drivers})

@login_required
def driver_detail(request, pk):
    driver = Driver.objects.get(pk=pk)
    return render(request, 'driver_detail.html', {'driver': driver})

@login_required
def driver_create(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm()
    return render(request, 'driver_form.html', {'form': form})

@login_required
def driver_update(request, pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'driver_form.html', {'form': form})

@login_required
def driver_delete(request, pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver_list')
    return render(request, 'driver_confirm_delete.html', {'driver': driver})
def profile(request):
    if request.method == 'POST':
        form =DriverForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid ():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('/')
    else:
        form = DriverForm(instance= request.user.profile)
    context = {'form':form}  
    return render (request,'TMSapp/driver.html', context)