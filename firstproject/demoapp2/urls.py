from django.urls import path

from . import views

urlpatterns = [
    path('a/', views.hello, name='hello'),
    ]