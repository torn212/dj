# example/urls.py
from django.urls import path

from example.views import index
from example.views import hello
from example.views import api

urlpatterns = [
    path('index', index),
    path('hello', hello),
    path('api', api)
]
