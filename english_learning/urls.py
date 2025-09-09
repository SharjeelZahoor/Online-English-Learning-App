# english_learning/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # our custom accounts app
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # django-allauth (social login, password reset, etc.)
    path('accounts/', include('allauth.urls')),
]

