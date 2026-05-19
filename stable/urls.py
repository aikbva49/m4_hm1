from django.urls import path
from . import views

urlpatterns = [
    path('stable/', views.TourListView.as_view(), name='tour_list'),
    path('stable/new/', views.TourCreateView.as_view(), name='tour_create'),
    path('stable/edit/<int:id>/', views.TourUpdateView.as_view(), name='tour_update'),
    path('stable/delete/<int:id>/', views.TourDeleteView.as_view(), name='tour_delete'),
]

