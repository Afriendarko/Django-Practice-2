from django.urls import path

from . import views

urlpatterns = [
    path('', views.tapp, name='tapp'),
]