from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.orm.mixins import TimestampModelMixin


class Target(TimestampModelMixin, models.Model):
    mission = models.ForeignKey(
        "Mission",
        on_delete=models.CASCADE,
        related_name="targets",
        verbose_name=_("mission"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("target name"),
    )
    country = models.CharField(
        max_length=255,
        verbose_name=_("country"),
    )  # Should be normalized using DB normal forms
    is_completed = models.BooleanField(
        default=False,
        verbose_name=_("target completed"),
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name} ({self.country}) - Mission #{self.mission.id}"
