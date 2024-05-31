from django.shortcuts import render
from django.http import HttpResponse
from .models import userModel,Product
# Create your views here.
def signup(request):
    return HttpResponse("This is signup api")

def login(request):
    return HttpResponse("This is login api")

def all_users(request):
    users=userModel.objects.all()
    all_data=[]
    for user in users:
        all_data.append(user.date_create)
    return HttpResponse(all_data)

def All_Products(request):
    products=Product.objects.all()
    print(products)
    Total_Price=0
    for i in range(0,len(products)):
       Total_Price+=products[i].price
    
    return HttpResponse(Total_Price)