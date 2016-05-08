# -*- coding: utf-8 -*-
from django.shortcuts import render
from products.models import Products

# Create your views here.
def index(request):
    return render(request,'index.html')
def contacts(request):
    product = Products.objects.get(id=8)
    return render(request,'Contacts.html',{'product':product})