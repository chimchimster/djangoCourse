from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Women, Category

# Create your views here.
menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add Article', 'url_name': 'add_page'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'Sign In', 'url_name': 'login'}
        ]
def index(request): #link to class HttpRequest
    posts = Women.objects.all()
    categories = Category.objects.all()
    return render(request, 'women/index.html', {
        'title': 'Main Page',
        'menu': menu,
        'posts': posts,
        'categories': categories,
        'cat_selected': 0,
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

def show_category(request, cat_id):

    posts = Women.objects.filter(cat_id=cat_id)
    categories = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    return render(request, 'women/index.html', {
        'title': 'Display by Categories',
        'menu': menu,
        'posts': posts,
        'categories': categories,
        'cat_selected': cat_id,
    })