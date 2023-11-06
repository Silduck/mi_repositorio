from django.shortcuts import render

from django.views import generic

from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'

def lista_de_posts(request):
    template = 'blog/index.html'
    contexto = {

        "posteos": Post.objects.filter(status=1).order_by('-created_on'),

    }
    return render(request, template, contexto)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html' 
