from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Women, Category


def index(request): #link to class HttpRequest
    posts = Women.objects.all()

    return render(request, 'women/index.html', {
        'title': 'Main Page',
        'posts': posts,
        'cat_selected': 0,
    })

def about(request):
    return render(request, 'women/about.html', {
        'title': 'About Site',
    })

def addpage(request):
    return HttpResponse('Adding Article')

def contact(request):
    return HttpResponse('Contacts')

def login(request):
    return HttpResponse('Signing In')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page doesn't found</h1>")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    return render(request, 'women/post.html', {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    })

def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug)

    if len(posts) == 0:
        raise Http404()

    return render(request, 'women/index.html', {
        'title': 'Display by Categories',
        'posts': posts,
        'cat_selected': cat_slug,
    })