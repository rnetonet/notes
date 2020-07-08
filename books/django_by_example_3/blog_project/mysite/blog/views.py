from django.shortcuts import render, get_object_or_404
from django.core.paginator import Page, Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm, PostShareForm

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)

    new_comment = False
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    return render(request, "blog/post/detail.html", {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form
    })


def post_share(request, pk):
    post = get_object_or_404(Post, pk=pk)
    email_sent = False

    if request.method == "GET":
        form = PostShareForm(initial={"post": post})
    else:
        form = PostShareForm(request.POST, initial={"post": post})
        if form.is_valid():
            form.send_email()
            email_sent = True

    return render(
        request,
        "blog/post/share.html",
        {"post": post, "form": form, "email_sent": email_sent},
    )
