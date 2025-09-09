from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=User.Roles.choices)

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')
