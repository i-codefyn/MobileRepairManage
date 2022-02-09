from employees import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.index, name="e-dashboard"),
    

]
urlpatterns += staticfiles_urlpatterns()