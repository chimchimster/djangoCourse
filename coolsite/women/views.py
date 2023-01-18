from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
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

def show_post(request, post_id):
    return HttpResponse(f'Showing article referenced with id = {post_id}')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    return render(request, 'women/index.html', {
        'title': 'Display by Categories',
        'posts': posts,
        'cat_selected': cat_id,
    })