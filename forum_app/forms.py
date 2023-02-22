from django import forms
from forum_app.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'topic', 'title',)
