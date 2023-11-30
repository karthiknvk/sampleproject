from django.shortcuts import render

from django.http import HttpResponse
from .models import Destination
# Create your views here.
#this home function is called by views.home in urls.py path()
def index(request):
  dests=Destination.objects.all
  return render(request,'index.html',{'dests':dests})

