import pytest

from everycheese.cheeses.models import Cheese

pytestmark = pytest.mark.django_db


def test_cheese_string_representation():
    cheese = Cheese.objects.create(
        name='Stracchino',
        description='A cheese',
        firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
