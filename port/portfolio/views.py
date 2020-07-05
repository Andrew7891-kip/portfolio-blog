from django.shortcuts import render
from .models import *
# Create your views here
def home(request):
    port=Portfolio.objects.all()
    return render(request,'home.html',{'port':port})

def index(request,pk):
    port=Portfolio.objects.get(pk=pk)
    return render(request,'index.html',{'port':port})

