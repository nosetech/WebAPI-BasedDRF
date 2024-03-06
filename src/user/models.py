import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_boost.models.manager import LogicalDeletionManager

from common.utils.models import TimeStampedModel


class UserManager(BaseUserManager, LogicalDeletionManager):
    use_in_migrations = True

    def _create_user(self, email, role, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.role = role
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, role, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, role, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, User.Role.ADMIN, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.EmailField(_("mail address"), unique=True)

    class Role:
        USER: int = 10
        STAFF: int = 20
        ADMIN: int = 99

    ROLE_CHOICES = (
        (Role.USER, "User"),
        (Role.STAFF, "Staff"),
        (Role.ADMIN, "Administrator"),
    )

    role = models.PositiveSmallIntegerField(_("role"), default=Role.USER, choices=ROLE_CHOICES)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        db_table = "users"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def is_staff(self):
        return True if self.role >= User.Role.ADMIN else False
