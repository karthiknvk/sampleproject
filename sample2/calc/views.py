from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
#this home function is called by views.home in urls.py path()
def home(request):
  return render(request,'home.html',{'name':'karthik'},)

def add(request):
  value1=int(request.POST['num1'])
  value2=int(request.POST['num2'])
  res=value1+value2
  return render(request,'result.html',{'result':res})