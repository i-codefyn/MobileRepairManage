
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request,'index.html')



def register(request):
    if request.method == "POST":
        if request.POST['password']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('e-dashboard')
        else:
            return render (request,'register.html', {'error':'Password does not match!'})
    else:
        return render(request,'register.html')
 

def login(request):
   if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('e-dashboard')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
   else:
        return render(request,'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')
