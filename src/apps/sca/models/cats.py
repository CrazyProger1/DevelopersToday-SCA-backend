from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Cat(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("name"),
        null=False,
        blank=False,
    )
    breed = models.CharField(
        max_length=255,
        verbose_name=_("breed"),
        null=False,
        blank=False,
    )
    experience = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(30),),
        verbose_name=_("experience"),
        help_text=_("Cat's experience in years."),
        default=0,
        blank=False,
        null=False,
    )
    salary = models.DecimalField(
        verbose_name=_("salary $"),
        help_text=_("Cat's salary in USD."),
        validators=(MinValueValidator(1),),
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=False,
    )
