from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomRegisterForm(UserCreationForm):
    captcha = CaptchaField(label='Введите текст с картинки')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'first_name', 
            'last_name', 
            'email', 
            'phone_number', 
            'gender',
            'birth_date', 
            'address', 
            'experience', 
            'skills', 
            'github_link', 
            'education', 
            'photo', 
            'resume'
        )

class CustomLoginForm(AuthenticationForm):
    captcha = CaptchaField(label='Вы человек?')