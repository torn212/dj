# example/urls.py
from django.urls import path

from example.views import index
from example.views import hello


urlpatterns = [
    path('', index),
    path('hello', hello),
    path('api', api)
]