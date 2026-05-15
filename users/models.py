from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = (('М', 'Мужской'), ('Ж', 'Женский'))
    
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255)
    experience = models.PositiveIntegerField(default=0)
    skills = models.TextField()
    github_link = models.URLField(blank=True)
    education = models.CharField(max_length=200)
    
    # 2 обязательных поля для файлов:
    photo = models.ImageField(upload_to='photos/')
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.username