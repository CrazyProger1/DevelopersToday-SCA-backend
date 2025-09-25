from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.orm.mixins import TimestampModelMixin


class Mission(TimestampModelMixin, models.Model):
    cat = models.OneToOneField(
        "Cat",
        on_delete=models.SET_NULL,
        related_name="mission",
        null=True,
        blank=True,
        verbose_name=_("assigned cat"),
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name=_("mission completed"),
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Mission #{self.pk} (Cat: {self.cat or 'Unassigned'})"
