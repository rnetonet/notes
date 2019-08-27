from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


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
            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        form = UserCreationForm()

    return render(request, "account/register.html", {"form": form})


@login_required()
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})
