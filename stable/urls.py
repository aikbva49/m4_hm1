from django.urls import path
from . import views

urlpatterns = [
    path('horses/', views.horse_list, name='horse_list'),
    path('horses/add/', views.horse_add, name='horse_add'),
    path('horses/edit/<int:pk>/', views.horse_edit, name='horse_edit'),
    path('horses/delete/<int:pk>/', views.horse_delete, name='horse_delete'),
]