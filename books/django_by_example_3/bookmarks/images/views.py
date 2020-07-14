import redis as redislib
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from actions.utils import create_action
from common.decorators import require_AJAX

from .forms import ImageCreateForm
from .models import Image


redis = redislib.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

# Create your views here.
@login_required
def image_create(request):
    form = ImageCreateForm(data=getattr(request, request.method) or None)

    if request.method == "POST" and form.is_valid():
        form = ImageCreateForm(data=request.POST or None)
        new_item = form.save(commit=False)
        new_item.user = request.user
        new_item.save()
        messages.success(request, "Image created successfully")

        create_action(request.user, "bookmarked image", new_item)

        return redirect(new_item.get_absolute_url())

    return render(
        request, "images/image/create.html", {"section": "images", "form": form}
    )


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    total_views = redis.incr(f"image:{image.id}:views")
    # score
    redis.zincrby(name="image_ranking", value=image.id, amount=1)

    return render(
        request, "images/image/detail.html", {"section": "images", "image": image, "total_views": total_views}
    )


@login_required
@require_POST
@require_AJAX
def image_like(request):
    image_id = request.POST.get("id")
    image = get_object_or_404(Image, id=image_id)

    total_likes = image.users_likes.count()

    action = request.POST.get("action")
    try:
        if action == "like":
            image.users_likes.add(request.user)
            total_likes += 1
            create_action(request.user, "liked", image)
        else:
            image.users_likes.remove(request.user)
            total_likes -= 1

        return JsonResponse({"status": "ok", "total_likes": total_likes})

    except:
        return JsonResponse({"status": "error"})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 2)

    page = request.GET.get("page", 1)
    try:
        images = paginator.page(page)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse("")
        else:
            images = paginator.page(images, paginator.num_pages)

    if request.is_ajax():
        return render(
            request,
            "images/image/list_ajax.html",
            {"images": images, "section": "images"},
        )
    else:
        return render(
            request, "images/image/list.html", {"images": images, "section": "images"}
        )
