# example/views.py

import requests
from django.http import HttpResponse


def index(request):
    return HttpResponse('index')


def hello(request):
    return HttpResponse('hello aaaaa')


def api(request):
    name = request.GET.get('name')
    r = requests.request(method='GET', url='https://api.twitter.com/1.1/users/show.json?screen_name=' + name,
                         headers={
                             'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAG7xqAEAAAAAhX%2FIUoT9ShGkFjPZWohUodOv6F4%3DiTI6bjcnwCsnQnHnPEwGFS2xQWkGeu6Q9oqsBrMOvZnGhE9jrt'})
    return HttpResponse(r.text)
