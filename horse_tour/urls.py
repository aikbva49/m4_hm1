from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.HorseTourListView.as_view(), name='tour_list'),
    path('create_review/', views.CreateReviewView.as_view(), name='create_review'),
]