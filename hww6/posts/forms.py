from django import forms
from posts.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text') 


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
         
class PostUpdateView(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']