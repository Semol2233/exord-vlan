from django.urls import path
from .views import *

urlpatterns = [
    path('fggvf',homeview,name='home'),
    path('form/',RegisterForms,name='hoggme'),
    path('',ASn_POst.as_view(),name='homssses'),
    path('list/',ASn_POst_listview.as_view(),name='homes'),

    path('up/<int:pk>/',postUpdate.as_view(),name='up'),
    path('del/<int:pk>/',postDelete.as_view(),name='del'),
    path('se/',SearchResultsView,name='serach'),





]