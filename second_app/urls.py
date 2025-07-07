from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('borrowed_books/', views.borrowed_books, name='borrowed_books'),   
]