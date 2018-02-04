from . models import Article, Comment
from django import forms


class BlogForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'description', 'image']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
