from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.django.orm.mixins import TimestampModelMixin


class Note(TimestampModelMixin, models.Model):
    target = models.ForeignKey(
        "Target",
        on_delete=models.CASCADE,
        related_name="notes",
        verbose_name=_("target"),
    )
    content = models.TextField(verbose_name=_("note content"))

    def __str__(self):
        return f"Note for Target: {self.target.name}"
