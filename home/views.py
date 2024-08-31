from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    now = datetime.now()
    html = f"<html><body><h1>It is now {now}.</h1></body></html>"
    return HttpResponse(html)

def hello(request):
    html = "<html><body><h1>Hello World!</h1></body></html>"
    return HttpResponse(html)