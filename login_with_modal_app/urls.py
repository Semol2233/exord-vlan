from django.urls import path
from .views import Home_modal

urlpatterns = [
  path('home',Home_modal.as_view(),name='home')

]