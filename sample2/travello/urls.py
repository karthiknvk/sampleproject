from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL pattern #because '' has no value,so itis default page
    
]
