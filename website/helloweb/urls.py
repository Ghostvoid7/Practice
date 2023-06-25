from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('django/', views.django),
    path('author/', views.about)
]







