from django.shortcuts import render

from django.http import HttpResponse
from .models import Destination
# Create your views here.
#this home function is called by views.home in urls.py path()
def index(request):
  dest1=Destination()
  dest1.name='Mumbai'
  dest1.desc='The city that never sleeps'
  dest1.price=800
  dest1.img='destination_1.jpg'
  dest1.offer='True'

  dest2=Destination()
  dest2.name='Hyderabad'
  dest2.desc='First Biryani,Then Sherwani '
  dest2.price=750
  dest2.img='destination_2.jpg'
  dest2.offer='False'

  dest3=Destination()
  dest3.name='Bangalore'
  dest3.desc='Beautiful city'
  dest3.price=730
  dest3.img='destination_3.jpg'
  dest3.offer='False'

  dests=[dest1,dest2,dest3]
  return render(request,'index.html',{'dests':dests})

