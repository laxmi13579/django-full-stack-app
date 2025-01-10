from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime 
from app1.forms import RegisterForm

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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('Name:',name)
            print('Email:',email)
            print('Password:',password)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    return render(request, 'app1/register.html', {'form': form})
