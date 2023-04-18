from django.shortcuts import render

# Create your views here.

# blog/views.py

from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
