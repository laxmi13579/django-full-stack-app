from django.http import HttpResponse


def index(request, **kwargs):
    status = kwargs.get('status')
    return HttpResponse(f'Hello Laxmi from Root {status}')