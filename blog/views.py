from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *


def index(request):
    bio = get_object_or_404(ShortBio)
    personal_interests = PersonalInterest.objects.all().order_by('rank')
    professional_interests = ProfessionalInterest.objects.all().order_by('rank')
    return render(request, 'blog/index.html', {'bio': bio,
                                               'per_ints': personal_interests,
                                               'pro_ints': professional_interests})

def articles(request):
    return render(request, 'blog/articles.html', {})


def projects(request):
    return render(request, 'blog/projects.html', {})


def resume(request):
    objective = Objective.objects.get()
    education_exps = EducationExperience.objects.get_queryset().order_by('-from_date')
    professional_exps = ProfessionalExperience.objects.get_queryset().order_by('-from_date')
    return render(request, 'blog/resume.html', {'objective': objective,
                                                'ed_exps': education_exps,
                                                'pro_exps': professional_exps})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date')
    return render(request, 'blog/articles.html', {'posts': posts})
