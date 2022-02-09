from django.shortcuts import render
from  home.models import AppDetails
from django.views.generic import TemplateView, CreateView,ListView

from django.http import HttpResponse


class HomePage(TemplateView):
     template_name = "home/index.html"
     

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'app_data':AppDetails.objects.all(),
            'page_title':'Home Page'
        }
        return context
    

class AboutUs(TemplateView):
    template_name = 'home/about_us.html'


class Services(TemplateView):
    template_name = 'home/services.html'


class QuoteRequests(CreateView):
    template_name ='quote_form.hmtl'

