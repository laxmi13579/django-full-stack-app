from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 

# Create your views here.


def main(request):
    return render(request, 'app1/main.html')

def about(request):
    return render(request, 'app1/about.html')

def contactUs(request):
    return render(request, 'app1/contactUs.html')
