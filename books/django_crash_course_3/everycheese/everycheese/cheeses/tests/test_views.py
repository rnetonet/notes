import pytest
from pytest_django.asserts import assertContains

from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

from everycheese.users.models import User

from ..views import CheeseCreateView, CheeseDetailView, CheeseListView, CheeseUpdateView
from .factories import cheese, user

pytestmark = pytest.mark.django_db

def test_add_title(client, user):
    client.force_login(user)
    response = client.get(reverse("cheeses:add"))
    assertContains(response, "Add Cheese")

def test_update_title(client, user, cheese):
    client.force_login(user)
    response = client.get(reverse("cheeses:update", kwargs={"slug": cheese.slug}))
    assertContains(response, "Update")

def test_update_view(client, user, cheese):
    client.force_login(user)
    url = reverse("cheeses:update", kwargs={"slug": cheese.slug})
    form_data = {
        "name": cheese.name,
        "description": "Something new",
        "firmness": cheese.firmness
    }
    response = client.post(url, form_data)
    cheese.refresh_from_db()
    assert cheese.description == "Something new"