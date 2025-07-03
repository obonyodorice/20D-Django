from django.urls import path
from . import views
     
urlpatterns = [
    path('', views.index, name='index'),
    path('attachee_list/', views.attachee_view, name='attachee_list'),
]