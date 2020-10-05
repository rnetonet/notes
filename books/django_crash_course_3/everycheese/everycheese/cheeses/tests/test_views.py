import pytest
from pytest_django.asserts import assertContains

from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

from everycheese.users.models import User

from ..views import CheeseCreateView, CheeseDetailView, CheeseListView
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db

