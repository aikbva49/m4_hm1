from django.db import models

class Horse(models.Model):
    name = models.CharField(max_length=50, verbose_name="Кличка лошади")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    health_status = models.CharField(
        max_length=100, 
        verbose_name="Состояние здоровья", 
        default="Здоров"
    )
    photo = models.ImageField(upload_to='horses/', null=True, blank=True)

    def __str__(self):
        return self.name