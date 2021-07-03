from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'
    #Listview adds (__list) to the context object, it can be overridden as well using context_object_name
    context_object_name = 'blog_posts'

class PostDetail(generic.DetailView):
   model = Post
   template_name = 'post_detail.html'
   #context_object_name = 'contectObjectName'
"""
class BlogPostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'post_detail.html'
    context_object_name = 'blog_posts'
    paginate_by = 15  # that is all it takes to add pagination in a Class Based View


class BlogPostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/detail.html'
    context_object_name = 'blog_post'
"""
