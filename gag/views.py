from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user

from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'gag/index.html', {'posts': posts})
    #
class DetailsView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'gag/details.html'

def like(request, id):
    post = get_object_or_404(Post, pk=id)
    post.likes = post.likes + 1
    post.save()
    posts = Post.objects.all()
    return render(request, 'gag/index.html', {'posts': posts})

def profile(request):
    user = get_user(request)
    return HttpResponse("HELLO" +user.username)

def register(request):
    return HttpResponse("HELLO")