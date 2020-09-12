from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
from .models import Post,coverphoto,videomo
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm,PostNews
# Create your views here.
from django.contrib.auth import authenticate



class homeview(LoginRequiredMixin, ListView):
    context_object_name = 'mydlist'
    model =Post
    template_name= 'home.html'
    
class temview(LoginRequiredMixin, ListView):
    context_object_name = 'mylist'
    model =Post
    template_name= 'news_video.html'


    def get_context_data(self, **kwargs):
        context = super(temview,self).get_context_data(**kwargs)
        context['video_list'] =  videomo.objects.filter().order_by('-id')[:2]
        context['coverphoto_view'] =  coverphoto.objects.filter().order_by('-id')[:1]

        return context
    queryset = Post.objects.filter().order_by('-id')[:10] 


class temviewtwo( LoginRequiredMixin,ListView):
    context_object_name = 'semol'
    model =Post
    template_name= 'post_details.html'
    queryset = Post.objects.filter()[:2] 

class Covggerphoto(LoginRequiredMixin,ListView):
    context_object_name = 'cover'
    model = coverphoto
    template_name= 'base.html'
    queryset = coverphoto.objects.filter().order_by('-id')[:1] 



class PostDetails(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetails,self).get_context_data(**kwargs)
        context['video_list'] =  videomo.objects.filter().order_by('-id')[:2]
        context['post_list'] =  Post.objects.filter().order_by('-id')[:2]
        context['post_list'] =  Post.objects.filter().order_by('-id')[:1]
        return context

class Videoview(LoginRequiredMixin, ListView):
    context_object_name = 'video'
    model = videomo
    template_name = 'video.html'
    def get_context_data(self, **kwargs):
        context = super(Videoview,self).get_context_data(**kwargs)
        context['coverphoto_view'] =  coverphoto.objects.filter().order_by('-id')[:1]
        return context
    queryset = videomo.objects.filter().order_by('-id')[:5] 
    

class VideoDdetails(LoginRequiredMixin,DetailView):
    context_object_name = 'Video_details'
    model = videomo
    def get_context_data(self, **kwargs):
        context = super(VideoDdetails,self).get_context_data(**kwargs)
        context['video_list'] =  videomo.objects.filter().order_by('-id')[:2]
        context['video_listone'] =  videomo.objects.filter().order_by('-id')[:5]
        context['video_listtwo'] =  videomo.objects.filter().order_by('-id')[1:2]
        

        return context

    template_name = 'video_detials.html'


class moviepart(ListView):
    context_object_name = 'movie'
    model = videomo
    template_name = 'movie.html'


class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    model = videomo
    template_name = 'uplode_news.html'

class PostCreatenews(LoginRequiredMixin, CreateView):
    form_class = PostNews
    model = Post
    template_name = 'uplode_news.html'

class Mainhomepageview(TemplateView):
    template_name = 'main_home-page.html'


class postUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostNews
    model = Post
    template_name = 'uplode_news.html'


class postDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_news.html'
    success_url = reverse_lazy('details_view')



class VideopostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = videomo
    template_name = 'uplode_news.html'


class VideopostDelete(LoginRequiredMixin, DeleteView):
    model = videomo
    template_name = 'video_delete_news.html'
    success_url = reverse_lazy('video-page')

def formsModal(request):
    if request.method == 'POST':
        title = request.POST['title']
        photo = request.POST['photo']
        body = request.POST['body']
        Web =  Post.objects.create(title=title,body=body,photo=photo,)
        return HttpResponseRedirect(reverse('video-page'))
    return render(request,'ddemo.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(username=username,password=password)
        if user:
            if user.is_active:
           
                return HttpResponseRedirect(reverse('homes'))
        else:
            return render(request,'registration/login.html',{'fail':True})
    else:
        return render(request,'login.html')

