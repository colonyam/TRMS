from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('tms_admin_dashboard/', views.tms_admin_dashboard, name='tms_admin_dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('driver_dashboard/', views.driver_dashboard, name='driver_dashboard'),
]
