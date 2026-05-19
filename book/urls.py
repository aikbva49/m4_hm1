from django.urls import path
from . import views 

urlpatterns = [
    path('qs1/', views.Qs1View.as_view(), name='qs1'),
    path('qs2/', views.Qs2View.as_view(), name='qs2'),
    path('qs3/', views.Qs3View.as_view(), name='qs3'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_id'),
]