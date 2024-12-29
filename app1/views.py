from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 

# Create your views here.


def main(request):
    return render(request, 'app1/main.html')


def filterInDjango(request):
    context = {
        'name': 'laxmi kumar yadav',
        'adress': 'Mithila Nagar Palika Ward No. 1',
        'currentDate': datetime.now()
    }
    return render(request, 'app1/filterInDjango.html', context)