from django.urls import path
from . import views 

urlpatterns = [
    path('qs1/', views.qs1, name='qs1'),
    path('qs2/', views.qs2, name='qs2'),
    path('qs3/', views.qs3, name='qs3'),
    path('book_list/', views.book_list_view, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_id'),
]