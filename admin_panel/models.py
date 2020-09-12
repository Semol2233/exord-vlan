from django.db import models
from django.shortcuts import render,redirect,reverse

# Create your models here.
class Category(models.Model):
    cetagory_name = models.CharField(max_length=255)
    def __str__(self):
        return self.cetagory_name
        
    def get_absolute_url(self):
        return reverse('cetagory_list')
    