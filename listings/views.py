from django.shortcuts import render

# Create your views here.

from .models import Property

from django.http import HttpResponse
from django.views.generic import *

def home(request):
    return HttpResponse("UrbanHub is running 🚀")

class PropertyListView(ListView):
    template_name="property_list.html"
    queryset=Property.objects.all()
