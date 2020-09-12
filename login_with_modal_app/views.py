from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home_modal(TemplateView):
    template_name = 'home.html'