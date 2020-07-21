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

def third(request):
    return render(request,"html/third.html",context={'data':"abhilash",'name':"raju"})

def fourth(request):
    fruits=["apple","banana","cherry","kiwi","orange"]
    return render(request,"html/fourth.html",{'fruits':fruits})
def fifth(request):
    return render(request,"html/fifth.html",{'a':10,'b':25})
    