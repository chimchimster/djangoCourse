from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Women

# Create your views here.
menu = ["About Site", "Add Article", "Feedback", "Sign In"]
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

def categories(request, catid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1>Articles under the categories</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f'<h1>Years Archive</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page doesn't found</h1>")
