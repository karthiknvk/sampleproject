from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL pattern #because '' has no value,so itis default page
    path('accounts/',include('accounts.urls')),
    
]
