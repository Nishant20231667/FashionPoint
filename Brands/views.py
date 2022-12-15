from django.shortcuts import render
from django.http import HttpResponse

def brands(request):
    return render(request, 'brands.html')

def home(request):
    return render(request, 'index.html')
def contactus(request):
    return render(request, 'contactus.html')
def brand(request):
    return render(request, 'index.html')
