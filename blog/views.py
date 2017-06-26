from django.shortcuts import render
from django.utils import timezone
from .models import Post


def index(request):
    return render(request, 'blog/index.html', {})

def articles(request):
    return render(request, 'blog/construction.html', {})

def projects(request):
    return render(request, 'blog/construction.html', {})

def resume(request):
    return render(request, 'blog/construction.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
            'published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
