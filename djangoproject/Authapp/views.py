from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def signup(request):
    return HttpResponse("This is signup api")

def login(request):
    return HttpResponse("This is login api")