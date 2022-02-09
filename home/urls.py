from home import views
from django.urls import path

from .import views
from django.conf import settings
from home.views import HomePage,AboutUs,Services
from django.conf.urls.static import static



urlpatterns = [
path('' , HomePage.as_view(), name='home'),
path('about_us',AboutUs.as_view(), name='about'),
path('services', Services.as_view(), name = 'services')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)