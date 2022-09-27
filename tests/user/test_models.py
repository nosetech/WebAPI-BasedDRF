import re

import pytest
from django.db import transaction
from django.db.utils import IntegrityError

from user.models import User


@pytest.mark.django_db
def test_is_empty():
    assert User.objects.all().count() == 0


@pytest.mark.django_db
def test_is_count_one():
    user = User(
        email="test@example.com",
        password="password",
        role=10,
    )
    user.save()
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_logical_delete():
    user = User(
        email="test@example.com",
        password="password",
        role=10,
    )
    user.save()
    User.objects.all().delete()
    assert User.objects.all().count() == 1
    assert User.objects.first().deleted_at is not None
    User.objects.all().delete(hard=True)
    assert User.objects.all().count() == 0


@pytest.mark.django_db
def test_is_exception():
    with transaction.atomic():
        with pytest.raises(IntegrityError) as e:
            user = User(
                email=None,
                password="password",
                role=10,
            )
            user.save()
    assert "cannot be null" in str(e)

    with transaction.atomic():
        with pytest.raises(IntegrityError) as e:
            user = User(
                email="test@example.com",
                password=None,
                role=10,
            )
            user.save()
    assert "cannot be null" in str(e)


@pytest.mark.django_db
def test_clean():
    user = User(
        email="TEST@EXAMPLE.COM",
        password="password",
        role=10,
    )
    user.clean()
    user.save()
    assert User.objects.first().email == "TEST@example.com"


@pytest.mark.django_db
def test_is_staff():
    admin = User(
        email="admin@example.com",
        password="password",
        role=99,
    )
    admin.save()

    other = User(
        email="user@example.com",
        password="password",
        role=98,
    )
    other.save()

    assert User.objects.filter(email="admin@example.com").first().is_staff is True
    assert User.objects.filter(email="user@example.com").first().is_staff is False
