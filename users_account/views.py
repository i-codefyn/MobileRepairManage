
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from  home.models import AppDetails
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth import logout
from django.views.generic import RedirectView

site_name = 'Fixenix Mobile Services'



class Index(LoginRequiredMixin,TemplateView):
    template_name = 'users/dashboard.html'
    

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'app_data':AppDetails.objects.all(),
            'page_title':'SignUp     Page'
        }
        return context
    

class Login(LoginView):
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'app_data':AppDetails.objects.all(),
            'page_title':'SignUp Page'
        }
        return context

class LogoutView(LogoutView):
    pass

# def register(request):
#     page_title = 'User Registration'
#     if request.method == "POST":
#         if request.POST['password']:
#             try:
#                 User.objects.get(username = request.POST['username'])
#                 return render (request,'register.html', {'error':'Username is already taken!'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
#                 auth.login(request,user)
#                 return redirect('user_dashboard')
#         else:
#             html = 'users/registration.html'
#             content = {
#                 'error':'Password does not match!',
#                 'page_title':page_title }
#             return render (request,html,content)
#     else:
        
#         html = 'users/register.html'
#         title = {
#             'page_title':page_title,
#             'site_name':site_name
#             }
#         return render(request, html, title)
 

# def login(request):
#    page_title = 'User Login'
#    if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
#         if user is not None:
#             auth.login(request,user)
#             return redirect('user_dashboard')
#         else:
#             return render (request,'users/login.html', {'error':'Username or password is incorrect!'})
#    else:
#         html = 'users/login.html'
#         title = {
#             'page_title':page_title,
#             'site_name':site_name
#             }
#         return render(request, html, title)


# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#     return redirect('home')

# class LogoutView(View):
#     def get(self, request):
#       if request.method == 'POST':
#          auth.logout(request)
      
