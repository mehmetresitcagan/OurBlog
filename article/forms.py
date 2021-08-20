from django import forms
from article.models import Article


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
