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

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,ab):
    a=ab.split(" ")
    sum=int(a[0])+int(a[1])
    return HttpResponse(str(sum))

def greater(request,c,d,e):
    if(c>d):
        if(c>e):
            return HttpResponse(c)
        else:
            return HttpResponse(e)
    else:
        if(d>e):
            return HttpResponse(d)
        else:
            return HttpResponse(e)

def strin(request,srt):
    o="aeiouAEIOU"
    vow=""
    const=""
    for i in srt:
        if i in o:
            vow+=i;
        else:
            const+=i;
    return render(request,"html/vowels.html",{'string':srt,'vowels':vow,'const':const})
    