from django.shortcuts import render


# Create your views here.

def post_list(requests):
    return render(requests, 'blog/post_list.html' , {})