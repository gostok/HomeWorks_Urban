from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


def show_post(request):
    posts = Post.objects.all()
    items_page = request.GET.get('items_page', 3)
    paginator = Paginator(posts, items_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post.html', {'page_obj': page_obj, 'items_page': items_page})