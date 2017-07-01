from django.shortcuts import render
from django.utils import timezone
from .models import Post, ShortBio, PersonalInterest, ProfessionalInterest


def index(request):
    bio = ShortBio.objects.get()
    personal_interests = PersonalInterest.objects.all().order_by('rank')
    professional_interests = ProfessionalInterest.objects.all().order_by('rank')
    return render(request, 'blog/index.html', {'bio': bio,
        'per_ints': personal_interests,
        'pro_ints': professional_interests})

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
