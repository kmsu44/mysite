from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post


def index(request):
    Post_list = Post.objects.order_by('-create_date')
    context = {'Post_list': Post_list}
    return render(request, 'pybo/main.html', context)


def detail(request, Post_id):
    post = get_object_or_404(Post, pk=Post_id)
    context = {'post': post}
    return render(request, 'pybo/productInfo.html', context)
