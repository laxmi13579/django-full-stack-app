from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 

# Create your views here.


def main(request):
    context = [
    {
        "id": 1,
        "name": "Xyzabcdeft",
        "email": "abcde@example.com",
        "age": 34,
        "address": {
            "street": "123 Main St",
            "city": "Springfield",
            "state": "IL",
            "zipcode": "62704"
        }
    }
    ]
    return render(request, 'app1/main.html', {'title': 'main page'})

def about(request):
    return render(request, 'app1/about.html')

def contactUs(request):
    return render(request, 'app1/contactUs.html')
