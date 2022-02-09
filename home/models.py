from django.db import models




class AppDetails(models.Model):
     app_name = models.CharField( max_length=100)
     app_email = models.CharField( max_length=100,blank =True , null =True)
     app_mobile = models.CharField( max_length=100, blank =True , null =True)
     app_web_address = models.CharField( max_length=70,blank =True , null =True)
     app_address = models.TextField( max_length=150,blank =True , null =True)
     app_version = models.FloatField()
     app_logo= models.FileField(upload_to='upload/', blank =True , null =True )
     app_fevicon= models.FileField(upload_to='upload/' , blank =True , null =True)
    
  