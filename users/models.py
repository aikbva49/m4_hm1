from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Дополнительные поля (всего с базовыми будет больше 10)
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    address = models.TextField(verbose_name="Адрес проживания")
    experience = models.PositiveIntegerField(default=0, verbose_name="Опыт работы (лет)")
    skills = models.TextField(verbose_name="Навыки")
    github_link = models.URLField(blank=True, verbose_name="Ссылка на GitHub")
    education = models.CharField(max_length=255, verbose_name="Образование")
    
    # 2 поля для файлов
    resume = models.FileField(upload_to='resumes/', verbose_name="Резюме (PDF/Doc)")
    photo = models.ImageField(upload_to='user_photos/', verbose_name="Фото профиля")

    def __str__(self):
        return f"{self.username} - {self.first_name}"