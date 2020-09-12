from django.urls import path
from .views import temview,PostDetails,temviewtwo,Covggerphoto,Videoview,VideoDdetails,moviepart,homeview,PostCreateView,PostCreatenews,Mainhomepageview,postUpdate,postDelete,VideopostUpdate,VideopostDelete,formsModal
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('grfgrg', Mainhomepageview.as_view(), name='mainpage'),  
    path('mainpage',homeview.as_view(),name='home'),
    path('details/',temview.as_view(),name='details_view'),
    path('=?/<int:pk>/',PostDetails.as_view(),name='details-page'),
    path('temviewtwo',temviewtwo.as_view(),name='temviewtwo'),
    path('cover',Covggerphoto.as_view(),name='coverphoto'),
    path('Videoview',Videoview.as_view(),name='video-page'),
    path('VideoDdetails/<int:pk>/',VideoDdetails.as_view(),name='video-details'),
    path('',LoginView.as_view(),name='login'),
    path('movie/',moviepart.as_view(),name='movie'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('uplode', PostCreateView.as_view(), name='uplode'),
    path('news/', PostCreatenews.as_view(), name='news-uplode'),  
    path('update/<int:pk>/', postUpdate.as_view(), name='news'),  
    path('delete/<int:pk>/', postDelete.as_view(), name='delete'), 
    path('updatevideo/<int:pk>/', VideopostUpdate.as_view(), name='updatevideo'),
    path('deletevideo/<int:pk>/', VideopostDelete.as_view(), name='deletevideos'),  
    path('del',formsModal, name='deletevgggideos'),  











    




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

