from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")
def home(request):
    return HttpResponse("<h1> welcome to home page<h1>")

def htmlout(request):
    return render(request,"out.html")

def htmlin(request):
    return render(request,"html/in.html")
    