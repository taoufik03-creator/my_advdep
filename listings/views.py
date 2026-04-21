from django.shortcuts import render

# Create your views here.

from .models import Property

from django.http import HttpResponse


def home(request):
    return HttpResponse("UrbanHub is running 🚀")


