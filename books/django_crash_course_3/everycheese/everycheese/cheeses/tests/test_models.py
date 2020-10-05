from everycheese.users.models import User
import pytest
from pytest_django.asserts import assertContains

from django.urls import reverse

from everycheese.cheeses.tests.factories import CheeseFactory, UserFactory
from everycheese.cheeses.models import Cheese

from ..views import (
    CheeseListView,
    CheeseDetailView,
)

pytestmark = pytest.mark.django_db

def test_good_cheese_detail_view(rf):
    cheese = CheeseFactory()
    url = reverse(
        "cheeses:detail",
        kwargs={"slug": cheese.slug}
    )
    request = rf.get(url)
    response = CheeseDetailView.as_view()(request, slug=cheese.slug)
    assertContains(response, cheese.name)

def test_good_cheese_list_view_expanded(rf):
    request = rf.get(reverse("cheeses:list"))
    response = CheeseListView.as_view()(request)
    assertContains(response, 'Cheese List')

def test_cheese_string_representation():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name

def test_get_absolute_url():
    cheese = CheeseFactory()
    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}/'


@pytest.fixture
def user():
    return UserFactory()

def test_good_cheese_create_view(client, user):
    client.force_login(user)
    url = reverse("cheeses:add")
    response = client.get(url)
    assert response.status_code == 200

def test_cheese_list_contains_2_cheeses(rf):
    cheese1 = CheeseFactory()
    cheese2 = CheeseFactory()

    request = rf.get(reverse("cheeses:list"))
    response = CheeseListView.as_view()(request)

    assertContains(response, cheese1.name)
    assertContains(response, cheese2.name)

def test_detail_contains_cheese_data(rf):
    cheese = CheeseFactory()
    request = rf.get(cheese.get_absolute_url())
    response = CheeseDetailView.as_view()(request, slug=cheese.slug)
    assertContains(response, cheese.name)
    assertContains(response, cheese.get_firmness_display())
    assertContains(response, cheese.country_of_origin.name)


def test_cheese_create_form_valid(client, user):
    client.force_login(user)
    form_data = {
        "name": "Paski Sir",
        "description": "A salty hard cheese",
        "firmness": Cheese.Firmness.HARD
    }
    url = reverse("cheeses:add")
    response = client.post(url, form_data)

    assert response.status_code == 302 # redirect

    cheese = Cheese.objects.get(name="Paski Sir")

    assert cheese.description == "A salty hard cheese"
    assert cheese.firmness == Cheese.Firmness.HARD
    assert cheese.creator == user
