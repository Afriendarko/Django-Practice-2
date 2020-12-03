from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tapp(request):
    context = {'tag_vars':"tag_vars"}
    return render(request,"demoapp/abc.html",context)

def get_name(request):
    form = NameForm()
    context = {'form':form}
    return render(request,'demoapp/abc.html',context)
