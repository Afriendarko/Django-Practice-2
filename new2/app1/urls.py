from django.urls import path
from . import views


urlpatterns = [
    path('a/', views.hello, name='hello'),
    path('t/',views.tapp, name='tapp'),
    path('f',views.get_name, name='get_name'),
    path('nf',views.fbf, name='fbf'),
    path('fs',views.listfeedback.as_view(),name='fs'),
    path('HomePage',views.HomePage.as_view(),name='HP'),
    # path('signup/',views.SignUpView.as_view(),name='signup'),
]
