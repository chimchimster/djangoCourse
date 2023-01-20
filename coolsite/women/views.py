from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Women, Category
from .forms import AddPostForm
from .utils import DataMixin


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main Page")
        return dict(list(context.items()) + list(c_def.items()))


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
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {
        'title': 'About Site',
        'page_obj': page_obj
    })


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add Page")
        return dict(list(context.items()) + list(c_def.items()))

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


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


"""
def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    return render(request, 'women/post.html', {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    })
"""


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Category - ' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id
        )
        return dict(list(context.items()) + list(c_def.items()))

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