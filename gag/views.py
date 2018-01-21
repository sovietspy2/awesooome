from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic

from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html' ,{'posts': posts})
    #return HttpResponse("hello world")

class detailsView(generic.DetailView):
    model = Post
    template_name = 'gag/details.html'