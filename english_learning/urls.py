# english_learning/urls.py
from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home_redirect, name='home'),
    # our custom accounts app
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # django-allauth (social login, password reset, etc.)
    path('accounts/', include('allauth.urls')),
    
    #learning 
    path('learning/', include('learning.urls', namespace='learning')),
    
]

