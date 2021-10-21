from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post

# Create your views here.
class InicioListView(View):
    def get(self, request, *args, **kwargs):
        context={}
        return render(request, 'inicio.html', context)

class InicioCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context = {
            'form' : form
        }
        return render(request, 'inicio_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title2 = form.cleaned_data.get('title')
                content2 = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title= title2, content= content2)
                p.save()
                return redirect('inicio:Home')
            context = {
                
                    
            }
        return render(request, 'inicio_create.html', context)

