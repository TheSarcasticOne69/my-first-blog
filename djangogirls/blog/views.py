from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def post_detail(requests,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(requests,'blog/post_detail.html',{"post" : post})

def post_list(requests):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(requests, 'blog/post_list.html' , {'posts' : posts})