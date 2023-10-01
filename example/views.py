# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    return HttpResponse('index')


def hello(request):
    return HttpResponse('hello aaaaa')


def api(request, name):
    return HttpResponse('hello :' + name)
