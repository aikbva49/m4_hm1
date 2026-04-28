from django.urls import path
from . import views 

urlpatterns = [
    path('qs1/', views.qs1, name='qs1'),
    path('qs2/', views.qs2, name='qs2'),
    path('qs3/', views.qs3, name='qs3'),
]