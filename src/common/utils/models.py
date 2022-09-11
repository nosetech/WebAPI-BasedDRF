from django.db import models
from django_boost.models.mixins import LogicalDeletionMixin


class TimeStampedModel(LogicalDeletionMixin):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
