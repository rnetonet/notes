from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from actions.models import Action
from actions.utils import create_action
from common.decorators import require_AJAX

from .forms import LoginForm, ProfileEditForm, UserEditForm
from .models import Contact, Profile


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(f"Welcome! {user.username}")
                else:
                    return HttpResponse(f"{user.username} is inactive")
            else:
                return HttpResponse("Invalid login / password")
    else:  # GET
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})


def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            create_action(new_user, "created an account")
            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        form = UserCreationForm()

    return render(request, "account/register.html", {"form": form})


@login_required
def dashboard(request):
    actions = Action.objects.exclude(user=request.user)

    following_ids = request.user.following.values_list("id", flat=True)
    if following_ids:
        actions = Action.objects.filter(user_id__in=following_ids)

    actions = actions.select_related('user', 'user__profile').prefetch_related("target")[:10]

    return render(
        request, "account/dashboard.html", {"section": "dashboard", "actions": actions}
    )


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Credentials saved with success")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(
        request,
        "account/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, "account/user/list.html", {"users": users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, "account/user/detail.html", {"user": user})


@login_required
@require_POST
@require_AJAX
def user_follow(request):
    username = request.POST.get("username")
    action = request.POST.get("action", "follow")

    if username and action:
        user = get_object_or_404(User, username=username)
        if action == "follow":
            Contact.objects.get_or_create(user_from=request.user, user_to=user)
            create_action(request.user, "started following", user)
            return JsonResponse(
                {"status": "ok", "total_followers": user.followers.count()}
            )
        else:
            Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse(
                {"status": "ok", "total_followers": user.followers.count()}
            )

    return JsonResponse({"status": "fail"})
