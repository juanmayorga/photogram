# Django
from django import forms
from django.forms import fields

# Model
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # forms settings
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
