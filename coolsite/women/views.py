from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Women, Category
from .forms import AddPostForm

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add Article', 'url_name': 'add_page'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'Sign In', 'url_name': 'login'}
        ]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main Page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

"""
def index(request): #link to class HttpRequest
    posts = Women.objects.all()

    return render(request, 'women/index.html', {
        'title': 'Main Page',
        'posts': posts,
        'cat_selected': 0,
    })
"""

def about(request):
    return render(request, 'women/about.html', {
        'title': 'About Site',
    })

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Add an Article"
        return context

"""
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {
        'title': "Adding an Article",
        'form': form,
    })
"""



def contact(request):
    return HttpResponse('Contacts')

def login(request):
    return HttpResponse('Signing In')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page doesn't found</h1>")


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = 'post_pk
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


"""
def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    return render(request, 'women/post.html', {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    })
"""


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

"""
def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug)

    if len(posts) == 0:
        raise Http404()

    return render(request, 'women/index.html', {
        'title': 'Display by Categories',
        'posts': posts,
        'cat_selected': cat_slug,
    })
"""