from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL pattern #because '' has no value,so itis default page
    path('add',views.add,name='add'),
]
