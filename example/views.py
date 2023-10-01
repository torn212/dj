# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    return HttpResponse('index')


def hello(request):
    return HttpResponse('hello aaaaa')


def api(request):
    return HttpResponse('hello :' + request.GET.get('name'))
