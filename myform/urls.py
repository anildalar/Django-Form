from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from . import views

#path(route, view, kwargs=None, name=None)

def myHomeFunc(request):
    
    return HttpResponse('<h1>Hello</h1>')    
urlpatterns = [
    path('',myHomeFunc),
    path('home/',views.myView)
]
