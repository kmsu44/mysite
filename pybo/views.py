import re
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .models import Category

from django.contrib.auth import views as auth_views
from django.core.paginator import Paginator

from django.db.models import Q

from django.http import HttpResponse
from django.views.decorators.http import require_POST


def index(request):
    page = request.GET.get('page', '1')
    Post_list = Post.objects.order_by('-create_date')

    # 정렬
    sort = request.GET.get('sort', '')
    if sort == 'like':
        Post_list = Post_list.order_by('-like_num')
    elif sort == 'Top_price':
        Post_list = Post_list.order_by('-dicount_price')
    elif sort == 'Low_price':
        Post_list = Post_list.order_by('dicount_price')
    else:
        Post_list = Post_list.order_by('-create_date')
        
        
    # 검색

    kw = request.GET.get('kw', '')  # 검색어

    if kw:
        Post_list = Post_list.filter(
            Q(title__icontains=kw)
            ).distinct()
    paginator = Paginator(Post_list, 8)
    page_obj = paginator.get_page(page)
    context = {'Post_list': page_obj,'page':page,'kw':kw}
    return render(request, 'pybo/main.html', context)




def cart(request):
    if request.user.is_authenticated:
        Post_list = Post.objects.order_by('-create_date')
        context = {'Post_list': Post_list}
        return render(request, 'pybo/cart.html', context)
    else:
        return render(request, 'common/login.html')

def Food(request):
    page = request.GET.get('page', '1')
    Post_list = Post.objects.filter(category=1)
    
    # 정렬
    sort = request.GET.get('sort','')
    if sort == 'like':
        Post_list = Post_list.order_by('-like_num')
    elif sort == 'Top_price':
        Post_list = Post_list.order_by('-dicount_price')
    elif sort == 'Low_price':
        Post_list = Post_list.order_by('dicount_price')
    else:
        Post_list = Post_list.order_by('-create_date')
    

    paginator = Paginator(Post_list, 8)
    page_obj = paginator.get_page(page)
    
    
    context = {'Post_list': page_obj}
    return render(request, 'pybo/Food.html', context)


def Stationery(request):
    page = request.GET.get('page', '1')
    Post_list = Post.objects.filter(category=7)
    sort = request.GET.get('sort','')
    if sort == 'like':
        Post_list = Post_list.order_by('-like_num')
    elif sort == 'Top_price':
        Post_list = Post_list.order_by('-dicount_price')
    elif sort == 'Low_price':
        Post_list = Post_list.order_by('dicount_price')
    else:
        Post_list = Post_list.order_by('-create_date')
    paginator = Paginator(Post_list, 8)
    page_obj = paginator.get_page(page)
    context = {'Post_list': page_obj}
    return render(request, 'pybo/Stationery.html', context)

def Etc(request):
    page = request.GET.get('page', '1')
    Post_list = Post.objects.filter(category=8)
    sort = request.GET.get('sort','')
    if sort == 'like':
        Post_list = Post_list.order_by('-like_num')
    elif sort == 'Top_price':
        Post_list = Post_list.order_by('-dicount_price')
    elif sort == 'Low_price':
        Post_list = Post_list.order_by('dicount_price')
    else:
        Post_list = Post_list.order_by('-create_date')
    paginator = Paginator(Post_list, 8)
    page_obj = paginator.get_page(page)
    context = {'Post_list': page_obj}
    return render(request, 'pybo/Etc.html', context)

def Clothes(request):
    page = request.GET.get('page', '1')
    Post_list = Post.objects.filter(category=9)
    sort = request.GET.get('sort','')
    if sort == 'like':
        Post_list = Post_list.order_by('-like_num')
    elif sort == 'Top_price':
        Post_list = Post_list.order_by('-dicount_price')
    elif sort == 'Low_price':
        Post_list = Post_list.order_by('dicount_price')
    else:
        Post_list = Post_list.order_by('-create_date')
    paginator = Paginator(Post_list, 8)
    page_obj = paginator.get_page(page)
    context = {'Post_list': page_obj}
    return render(request, 'pybo/Clothes.html', context)
# def join(request, post_id):

def Book(request):
    page = request.GET.get('page', '1')
    Post_list = Post.objects.filter(category=2)
    sort = request.GET.get('sort','')
    if sort == 'like':
        Post_list = Post_list.order_by('-like_num')
    elif sort == 'Top_price':
        Post_list = Post_list.order_by('-dicount_price')
    elif sort == 'Low_price':
        Post_list = Post_list.order_by('dicount_price')
    else:
        Post_list = Post_list.order_by('-create_date')
    paginator = Paginator(Post_list, 8)
    page_obj = paginator.get_page(page)
    context = {'Post_list': page_obj}
    return render(request, 'pybo/Book.html', context)


def joined(request):
    if request.user.is_authenticated:
        Post_list = Post.objects.order_by('-create_date')
        context = {'Post_list': Post_list}
        return render(request, 'pybo/joined.html', context)
    else:
        return render(request, 'common/login.html')

def detail(request, Post_id):
    post = get_object_or_404(Post, pk=Post_id)
    context = {'post': post}
    return render(request, 'pybo/productInfo.html', context)



    
    

def join(request, Post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk = Post_id)
    if request.user in post.joined_users.all():
        post.joined_users.remove(request.user)
        if post.participants != 0:
            post.participants -=1
        post.save()
    else:
        post.joined_users.add(request.user)
        post.participants +=1
        post.save()
    return redirect('pybo:index')

def like(request, Post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk = Post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        if post.like_num != 0:
            post.like_num -=1
            post.save()
    else:
        post.like.add(request.user)
        post.like_num +=1
        post.save()
    return redirect('pybo:index')

def Delete(request, Post_id):
    post = get_object_or_404(Post, pk = Post_id)
    post.delete()
    return redirect('pybo:cart')


def create(request):
    if request.method == "POST":

        post=Post(  user=request.user,
                    # category=request.POST.get('category'),
                    title=request.POST.get('title'),
                    price=request.POST.get('price'),
                    participants=0,
                    recruit_num=request.POST.get('recruit_num'),
                    category=Category.objects.get(sort=request.POST.get('category')),
                    dicount_price=request.POST.get('dicount_price'),
                    content=request.POST.get('content'),
                    image=request.FILES.get('image'))
        post.save()
        return redirect('pybo:index')
    else:
        return render(request, 'pybo/group.html')
    
