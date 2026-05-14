from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField() # Доп задание на 10 баллов

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'first_name', 'last_name', 'email', 'phone_number', 
            'birth_date', 'address', 'experience', 'skills', 
            'github_link', 'education', 'resume', 'photo'
        )

class CustomAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()