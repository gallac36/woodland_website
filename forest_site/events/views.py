from django.shortcuts import render
from django.views import generic
from .models import Event
from django.views.generic import ListView, DetailView, View

# Create your views here.
#def events (request):
#	return render(request, 'events.html')
	#return HttpResponse("<h1>MyClub Event Calendar</h1>")

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('-day')
    template_name = 'events.html'
    #Listview adds (__list) to the context object, it can be overridden as well using context_object_name
    context_object_name = 'event_posts'

class EventDetail(generic.DetailView):
   model = Event
   template_name = 'event_detail.html'


"""
def page(request, slug):
    try:
        page = Event.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'late_event.html', {'page': page})

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
