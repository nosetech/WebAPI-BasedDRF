import pytest
from django.contrib.auth.models import User


def test_one_plus_one():
    number = 1 + 1
    assert number == 2


@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username="system")
    assert me.is_superuser
