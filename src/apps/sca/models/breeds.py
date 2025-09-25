from django.db import models
from django.utils.translation import gettext_lazy as _


class Breed(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name=_("name"),
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Breed")
        verbose_name_plural = _("Breeds")

    def __str__(self):
        return self.name
