from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView

class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'
# Create your views here.

class HomePage(TemplateView):
    template_name= "home.html"
