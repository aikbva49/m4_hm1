from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.horse_tour_list_view, name='tour_list'),
    path('create_review/', views.create_review_view, name='create_review'),
]