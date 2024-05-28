from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    #return HttpResponse("well come to Django home page")
    return render(request,'page.html')

def About(request):
    #return HttpResponse("well come to Django About page")
    return render(request,'about.html')

def Contact(request):
    # return HttpResponse("well come to Django Contact page")
    return render(request,'contact.html')
