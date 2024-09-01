from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def hello(request):
    html = "<html><body><h1>Hello World!</h1></body></html>"
    return HttpResponse(html)
