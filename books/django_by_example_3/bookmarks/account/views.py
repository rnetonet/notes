from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

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
        instance=request.user.profile, data=request.POST or None, files=request.FILES or None
    )

    if request.method == "POST":
        if user_edit_form.is_valid() and user_profile_form.is_valid():
            user_edit_form.save()
            user_profile_form.save()

            messages.success(request, 'Profile update!')
        else:
            messages.error(request, 'Error updating your profile.')

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
