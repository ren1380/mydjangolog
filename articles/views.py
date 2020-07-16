from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.

def articles_list(request):
    articles = models.Articles.objects.all().order_by('date')
    args = {'articles':articles}
    return render(request, 'articles/articles_list.html', args)

def articles_detail(request, slug):
    return(HttpResponse(slug))
