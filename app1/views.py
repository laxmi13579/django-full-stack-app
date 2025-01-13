from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime 
from app1.forms import RegisterForm
from app1.models import Profile
# Create your views here.


def main(request):
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
            # save data into database
            user = Profile(name=name, email=email, password=password)
            user.save()

             # update data into database
            # user = Profile(id=1, name=name, email=email, password=password)
            # user.save()

             # delete data into database
            # user = Profile(id=1)
            # user.delete()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    return render(request, 'app1/register.html', {'form': form})
