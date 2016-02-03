from django.db import models
from django import forms
from django.utils import timezone
from django.forms.models import modelform_factory
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
#    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
#    published_date = models.DateTimeField(blank=True, null=True)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
    
class Rasp(models.Model):
    lesson = models.CharField(verbose_name="Урок", max_length=200)
    class_name = models.CharField(verbose_name="Класс",max_length=5)
    org_day = models.CharField(verbose_name="какой по счету урок", max_length=3)
    weekday = models.CharField( verbose_name="день недели", max_length=20)
    

class UploadFile(models.Model):
    fileplan = models.FileField(upload_to='plan/%Y/%m/')