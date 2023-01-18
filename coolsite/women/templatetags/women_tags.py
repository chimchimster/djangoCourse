from django import template
from women.models import Women, Category

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/menu.html')
def main_menu():
    menu = [{'title': 'About', 'url_name': 'about'},
            {'title': 'Add Article', 'url_name': 'add_page'},
            {'title': 'Contacts', 'url_name': 'contact'},
            {'title': 'Sign In', 'url_name': 'login'}
            ]
    return {'menu': menu}
