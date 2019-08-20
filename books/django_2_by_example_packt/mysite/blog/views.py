from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 1
    template_name = "blog/post/list.html"

# def post_list(request):
#     posts = Post.published.all()
#
#     paginator = Paginator(posts, 1)
#     page = request.GET.get("page")
#
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     context = {
#         "posts": posts
#     }
#     return render(request, "blog/post/list.html", context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post
    )
    context = {"post": post}

    return render(request, "blog/post/detail.html", context)