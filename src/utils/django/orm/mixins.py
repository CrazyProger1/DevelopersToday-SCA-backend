from django.conf import settings
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CreatedAtModelMixin(models.Model):
    created_at = models.DateTimeField(
        null=False,
        blank=False,
        auto_now_add=True,
        verbose_name=_("created at"),
        help_text=_("The date and time this object was created."),
    )

    class Meta:
        abstract = True


class UpdatedAtModelMixin(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated at"),
        help_text=_("The date and time this object was updated."),
    )

    class Meta:
        abstract = True


class TimestampModelMixin(CreatedAtModelMixin, UpdatedAtModelMixin):
    class Meta:
        abstract = True
