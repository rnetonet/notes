from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from actions.models import Action
from actions.utils import create_action
from common.decorators import require_AJAX

from .forms import UserEditForm, UserProfileForm, UserRegistrationForm
from .models import Contact, Profile


# Create your views here.
@login_required()
def dashboard(request):
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list("id", flat=True)

    if following_ids:
        actions.filter(user_id__in=following_ids)

    actions = actions.select_related("user", "user__profile").prefetch_related("target")
    actions = actions[:10]

    return render(
        request, "account/dashboard.html", {"section": "dashboard", "actions": actions}
    )


@login_required
def edit(request):
    user_edit_form = UserEditForm(instance=request.user, data=request.POST or None)
    user_profile_form = UserProfileForm(
        instance=request.user.profile,
        data=request.POST or None,
        files=request.FILES or None,
    )

    if request.method == "POST":
        if user_edit_form.is_valid() and user_profile_form.is_valid():
            user_edit_form.save()
            user_profile_form.save()

            messages.success(request, "Profile update!")
        else:
            messages.error(request, "Error updating your profile.")

    return render(
        request,
        "account/edit.html",
        {"user_edit_form": user_edit_form, "user_profile_form": user_profile_form},
    )


def register(request):
    form = UserRegistrationForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html", {"new_user": new_user})

    return render(request, "account/register.html", {"form": form})


@login_required
def user_list(request):
    User = get_user_model()
    users = User.objects.filter(is_active=True)
    return render(
        request, "account/user/list.html", {"users": users, "section": "people"}
    )


@login_required
def user_detail(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username, is_active=True)
    return render(
        request, "account/user/detail.html", {"user": user, "section": "people"}
    )


@require_AJAX
@require_POST
@login_required
def user_follow(request):
    User = get_user_model()

    user_id = request.POST.get("id")
    action = request.POST.get("action")

    if user_id and action:
        try:
            user = get_object_or_404(User, id=user_id)
            if action == "follow":
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                create_action(request.user, "started following", user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()

            total_followers = user.followers.count()

            return JsonResponse(
                {"status": "ok", "action": action, "total_followers": total_followers}
            )
        except User.DoesNotExist:
            return JsonResponse({"status": "error"})

    return JsonResponse({"status": "error"})
