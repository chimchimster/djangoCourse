from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Women

# Create your views here.
menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add Article', 'url_name': 'add_page'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'Sign In', 'url_name': 'login'}
        ]
def index(request): #link to class HttpRequest
    posts = Women.objects.all()
    return render(request, 'women/index.html', {
        'title': 'Main Page',
        'menu': menu,
        'posts': posts,
    })

def about(request):
    return render(request, 'women/about.html', {
        'title': 'About Site',
        'menu': menu,
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