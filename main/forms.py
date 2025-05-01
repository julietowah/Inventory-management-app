# forms.py

from .models import CustomUser
# main/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )




from django.contrib.auth.forms import UserCreationForm


class CustomRegistrationForm(UserCreationForm):
    # Additional fields for registration
    phone_number = forms.CharField(max_length=15, required=False, label="Phone Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # bio = forms.CharField(required=False, label="Bio", widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'phone_number')

        
