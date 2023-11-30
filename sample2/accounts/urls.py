from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),  # Root URL pattern #because '' has no value,so itis default page
    
]
