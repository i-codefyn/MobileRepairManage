# Generated by Django 4.0.1 on 2022-01-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_appdetails_delete_appname'),
    ]

    operations = [
        migrations.AddField(
            model_name='appdetails',
            name='app_address',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='appdetails',
            name='app_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appdetails',
            name='app_mobile',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appdetails',
            name='app_web_address',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='appdetails',
            name='app_name',
            field=models.CharField(max_length=100),
        ),
    ]
