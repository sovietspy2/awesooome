from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'gag/index.html', {'posts': posts})


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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            succes_message = 'You have been automatically logged in!'
            return render(request, 'gag/index.html', {'message': succes_message})
    else:
        form = UserCreationForm()
    return render(request, 'gag/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponse("Logged out!")


def create(request):
    return HttpResponse('200')