# accounts/urls.py
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path("dashboard-redirect/", views.dashboard_redirect, name="dashboard_redirect"),
    path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard")

]