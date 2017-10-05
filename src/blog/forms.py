from django import forms

from .models import Article, Tag


class ArticleForm(forms.Form):
    tags = forms.MultipleChoiceField(
            choices=Tag.objects.values_list('tag', flat=True)
        )
    publish_date = forms.DateTimeField()
    content = forms.CharField(min_length=5)
