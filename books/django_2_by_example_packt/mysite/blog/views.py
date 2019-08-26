from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
)
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .forms import CommentForm, EmailPostForm, SearchForm
from .models import Comment, Post


# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 1
    template_name = "blog/post/list.html"


def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_vector = SearchVector("title", weight="A") + SearchVector(
                "body", weight="B"
            )

            search_query = form.cleaned_data["query"]
            search_query = SearchQuery(query)

            results = (
                Post.objects.annotate(similarity=TrigramSimilarity("title", query))
                .filter(similarity__gte=0.1)
                .order_by("-similarity")
            )

    return render(
        request,
        "blog/post/search.html",
        {"form": form, "query": query, "results": results},
    )


def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = f"{data['name']} ({data['email']}) recommends to you the article {post.title}"
            message = f"""
                Read: {post.title} at {post_url}.

                {data['name']} comments:
                {data['comments']}
            """
            send_mail(
                subject, message, "admin@blog.me", [data["to"]], fail_silently=False
            )
            sent = True
    else:
        form = EmailPostForm()

    context = {"post": post, "form": form, "sent": sent}

    return render(request, "blog/post/share.html", context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=post,
    )

    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": post.comments.filter(active=True),
        "new_comment": new_comment,
        "comment_form": comment_form,
    }
    return render(request, "blog/post/detail.html", context)
