import pytest

from user.models import User


@pytest.fixture(scope="session", autouse=True)
def scope_sesstion(django_db_blocker):
    django_db_blocker.unblock()


@pytest.fixture(scope="function", autouse=True)
def scope_function():
    User.objects.all().delete(hard=True)
