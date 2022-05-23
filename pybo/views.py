from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .models import Category

from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')
    Post_list = Post.objects.order_by('-create_date')
    paginator = Paginator(Post_list, 8)
    page_obj = paginator.get_page(page)
    context = {'Post_list': page_obj}
    return render(request, 'pybo/main.html', context)


def detail(request, Post_id):
    post = get_object_or_404(Post, pk=Post_id)
    context = {'post': post}
    return render(request, 'pybo/productInfo.html', context)

# def create(request):
#     return render(request,'pybo/group.html')


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
                    content=request.POST.get('content'))

        post.save()
        return redirect('pybo:index')
    else:
        return render(request, 'pybo/group.html')


def joined(request):
    if request.user.is_authenticated:
        Post_list = Post.objects.order_by('-create_date')
        context = {'Post_list': Post_list}
        return render(request, 'pybo/joined.html', context)
    else:
        return render(request, 'common/login.html')

