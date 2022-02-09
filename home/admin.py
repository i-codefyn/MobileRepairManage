from django.contrib import admin

from home.models import AppDetails

class AppDetailsAdmin(admin.ModelAdmin):
    list_display =['app_name','app_version','app_logo','app_fevicon',
    'app_email','app_mobile','app_web_address','app_address']
admin.site.register(AppDetails, AppDetailsAdmin)

