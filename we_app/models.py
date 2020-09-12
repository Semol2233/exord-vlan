from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    photo = models.ImageField(upload_to='profile_pic', blank=True)
    timestamp = models.DateTimeField(auto_now_add= True,blank=True)
    updated= models.DateTimeField(auto_now= True,blank=True)
    
    def get_absolute_url(self):
        return reverse('details_view')
    
    def __str__(self):
        return self.title


class coverphoto(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile_pic', blank=True)


    def __str__(self):
        return self.title

class videomo(models.Model):
    title = models.CharField(max_length=255)
    clip = models.FileField(upload_to='user_video/',null=True)
    photo = models.ImageField(upload_to='profile_thub', blank=True)
    

    def get_absolute_url(self):
        return reverse('video-page')

    def __str__(self):
        return self.title
        



# Create your models here.m
