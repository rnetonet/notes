from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

import redis
from actions.utils import create_action
from common.decorators import require_AJAX

from .forms import ImageCreateForm
from .models import Image

# Redis
r = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)

# Create your views here.
@login_required
def image_create(request):
    if request.method == "POST":
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()

            create_action(request.user, "bookmarked image", new_item)
            messages.success(request, "Image added successfully")

            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)

    return render(request, "images/image/create.html", {"form": form})


@login_required
def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    total_views = r.incr(f"image:{image.id}:views")
    r.zincrby("image_ranking", image.id, 1)
    return render(
        request,
        "images/image/detail.html",
        {"image": image, "total_views": total_views},
    )


@login_required
@require_POST
@require_AJAX
def image_like(request):
    image_id = request.POST.get("id")
    action = request.POST.get("action", "like")

    if image_id and action:
        image = Image.objects.get(id=image_id)
        if action == "like":
            image.users_like.add(request.user)
            create_action(request.user, "likes", image)
        else:
            image.users_like.remove(request.user)
        return JsonResponse({"status": "ok", "count": image.users_like.count()})

    return JsonResponse({"status": "fail"})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, per_page=2)
    current_page = request.GET.get("page", 1)

    try:
        images = paginator.page(current_page)
    except EmptyPage:
        if request.is_ajax():
            return HttpResponse("")

        images = paginator.page(paginator.num_pages)  # Last page

    if request.is_ajax():
        return render(request, "images/image/list_ajax.html", {"images": images})

    return render(request, "images/image/list.html", {"images": images})

@login_required
def image_ranking(request):
    image_ranking = r.zrange("image_ranking", 0, -1, desc=True)
    map_id_score = {int(id):score for id, score in image_ranking}
    ids = list(map_id_score.keys())

    images = list(Image.objects.filter(id__in=ids))

    images.sort(key=lambda img: map_id_score[img.id])

    return render(request, "images/image/ranking.html", {"images": images})
