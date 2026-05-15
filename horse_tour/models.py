from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ServiceHorse(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TourCompany(models.Model):
    title = models.CharField(max_length=50, default='Elite Horse Tour')
    services = models.ManyToManyField(ServiceHorse, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.marks for r in reviews) / reviews.count(), 1)
        return 0


class Tourist(models.Model):
    name = models.CharField(max_length=100, default='Tourist Name')
    horse_nickname = models.CharField(max_length=100, default='Spirit')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}---{self.horse_nickname}'


class ReviewTour(models.Model):
    choice_company = models.ForeignKey(TourCompany, on_delete=models.CASCADE, related_name='reviews')
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, related_name='my_reviews', null=True)
    
    marks = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(1, message="Оценка только от 1 до 5"),
            MaxValueValidator(5, message="Оценка только от 1 до 5")
        ]
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_company}---{self.marks}'