from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Pengguna

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Pengguna
        fields = ("email", "Nama", "password1", "password2")
