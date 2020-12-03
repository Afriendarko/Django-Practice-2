from django.shortcuts import render

# Create your views here.

def tapp(request):
    context = {'tag_vars':"tag_vars"}
    return render(request,"app1/index.html",context)

