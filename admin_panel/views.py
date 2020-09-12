from django.shortcuts import render,redirect,reverse
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
from .forms import Cetagory_form
from .models import Category

# Create your views here.
def homeview(request):
    return render(request,'admin_home.html')

def imdexhome(request):
    return render(request,'index.html')

class Testing(TemplateView):
    template_name = 'testing.html'


class BookCreateView(CreateView):
    template_name = 'catagoy.html'
    form_class = Cetagory_form

    # def get_context_data(self, **kwargs):
    #     context = super(BookCreateView,self).get_context_data(**kwargs)
    #     context['catagory_list'] =Category.objects.filter().order_by('-id')[:1]
    #     return context
    

    # def get(self, request, *args, **kwargs):
    #     context = {'form': BookCreateForm()}
    #     return render(request, 'books/book-create.html', context)

    # def CetagoryAdd(request):
    #     Regsiter = False
    #     if request.method == 'POST':
    #         Cetagory_forms = Cetagory_form(data=request.POST)
    #         if Cetagory_forms.is_valid():
    #             Cetagory_forms.save()
    #             return redirect('cetagory_add')
    #         Regsiter = True
    #     else:
    #          Cetagory_forms = Cetagory_form()
    #      return render(request,'catagoy.html',{'forms':Cetagory_forms,'reg':Regsiter,})



        

class CcetagoryView(ListView):
    context_object_name = 'catagory_list'
    model = Category
    template_name = 'ceatgorylist.html'

