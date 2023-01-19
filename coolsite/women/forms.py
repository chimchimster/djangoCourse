from django import forms
from .models import Women, Category


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label="Celebrity Name",
        widget=forms.TextInput(attrs={'class': 'form-input'}
    ))
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 60, 'rows': 10}
        ),
        label="Article content"
    )
    is_published = forms.BooleanField(
        label="Publishing",
        required=False,
        initial=True,
    )
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Category",
        empty_label="Category is not chosen"
    )