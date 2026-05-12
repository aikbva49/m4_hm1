from django.db import models
from horse_tour.models import Company

class Orders(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО клиента')
    choice_company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE,
        verbose_name='Выбор компании'
    )
    number_card = models.PositiveIntegerField(default=12345678, verbose_name='Номер карты')
    photo = models.ImageField(upload_to='orders/', null=True, blank=True, verbose_name='Фото к заказу')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"Заказ от {self.name} (Компания: {self.choice_company})"