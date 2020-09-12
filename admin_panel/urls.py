from django.urls import path
from .views import homeview,imdexhome,Testing,BookCreateView,CcetagoryView

urlpatterns = [
    path('',imdexhome,name='home_admin'),
    path('second_home',homeview,name='home_ffadmin'),
    path('test',Testing.as_view(),name='home_dmin'),
    path('add/',BookCreateView.as_view(),name='cetagory_add'),
    path('Listc/',CcetagoryView.as_view(),name='cetagory_list'),




   

]