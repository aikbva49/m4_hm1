from django.urls import path
from . import views

urlpatterns = [
    path('stable/', views.tour_list, name='tour_list'),
    path('stable/new/', views.tour_create, name='tour_create'),
    path('stable/edit/<int:id>/', views.tour_update, name='tour_update'),
    path('stable/delete/<int:id>/', views.tour_delete, name='tour_delete'),
]

