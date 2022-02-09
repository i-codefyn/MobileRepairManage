from users_account import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', views.Index.as_view(), name="user_dashboard"),
    

]
urlpatterns += staticfiles_urlpatterns()