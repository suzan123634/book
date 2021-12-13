from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.HomeView, name='index'),
]
