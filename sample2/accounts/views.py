from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
  if request.method=='POST':
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    username=request.POST['username']
    email=request.POST['email']
    password1=request.POST['password']
    password2=request.POST['confirmpassword']

    if password1==password2:
      if User.objects.filter(username=username).exists():
        print('user name exist already')
      else:
        if User.objects.filter(email=email).exists():
          print('email exist already')
        else:
          user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
          user.save()
          print('user created')
    else:
      print("password not matching")
      
    return redirect('/')

  else:
    return render(request,"register.html")