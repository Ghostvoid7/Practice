from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('form.html/', views.form),
    path('form.html/save', views.save)
]








