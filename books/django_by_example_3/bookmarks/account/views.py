from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import UserEditForm, UserProfileForm, UserRegistrationForm
from .models import Profile


# Create your views here.
@login_required()
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})


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
    return render(request, "account/user/list.html", {"users": users, "section": "people"})

@login_required
def user_detail(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, "account/user/detail.html", {"user": user, "section": "people"})