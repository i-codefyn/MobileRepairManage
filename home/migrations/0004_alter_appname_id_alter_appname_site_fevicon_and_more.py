# Generated by Django 4.0.1 on 2022-01-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220126_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appname',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='appname',
            name='site_fevicon',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='appname',
            name='site_logo',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
