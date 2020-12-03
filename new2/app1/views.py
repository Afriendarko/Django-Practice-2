from django.shortcuts import render
from .forms import NameForm, feedbackform
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Thanks your data is added")

def tapp(request):
    context = {'tag_vars':"tag_vars"}
    return render(request,"app1/abc.html",context)

def get_name(request):
    form = NameForm()
    context = {'form':form}
    return render(request,'app1/abc.html',context)

def fbf(request):
    form = feedbackform(request.POST or None)
    if form.is_valid():
        form.save()
        form = feedbackform()

    context = {'form1':form}
    return render(request,'app1/newabc.html',context)

from rest_framework import generics, viewsets
from .serializer import feedbackserializer, studentsserializer
from .models import feedback, students
from django.views.generic import TemplateView

class listfeedback(generics.ListAPIView):
    queryset = feedback.objects.all()
    serializer_class = feedbackserializer

class feedbackview(viewsets.ModelViewSet):
    queryset = feedback.objects.all()
    serializer_class = feedbackserializer

class studentsview(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class = studentsserializer

class HomePage(TemplateView):
    template_name= "app1/demo.html"

# from django.views.generic.edit import CreateView
# from django.urls import reverse_lazy
#
# class SignUpView(CreateView):
#     form_class=CustomUserCreationForm
#     success_url=reverse_lazy("login")
#     template_name='signup.html'