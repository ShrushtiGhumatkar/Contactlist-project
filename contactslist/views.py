from django.shortcuts import render

from django.http import HttpResponse
from .models import Contact

def index(request):
    return HttpResponse('Hello')

def display(request):
    contacts = Contact.objects.all()
    return render(request,'index.html',{'list':contacts})



