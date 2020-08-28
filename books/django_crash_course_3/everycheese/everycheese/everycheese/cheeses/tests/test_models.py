import pytest

from everycheese.cheeses.models import Cheese
from everycheese.cheeses.tests.factories import CheeseFactory

pytestmark = pytest.mark.django_db


def test_cheese_string_representation():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
