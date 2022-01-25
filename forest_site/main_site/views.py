from django.http import HttpResponse
from django.shortcuts import render

"""View function for home page of site."""
def index(request):
	 # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def about (request):
#    return HttpResponse ('about')
    return render(request, 'about.html')

#def events (request):
#    return HttpResponse ('events')
 #   return render(request, 'events.html')

def firewood (request):
#    return HttpResponse ('firewood')
	return render(request, 'firewood.html')

def join (request):
#    return HttpResponse ('join')
    return render(request, 'join.html')

def archive (request):
    return render(request, 'archive.html')

def archivefiles (request):
    return render(request, 'archivefiles.html')
