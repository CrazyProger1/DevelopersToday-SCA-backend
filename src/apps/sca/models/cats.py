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
    )  # Should be normalized using DB normal forms
    image = models.ImageField(
        upload_to="cats/",
        verbose_name=_("image"),
        help_text=_("Cat's image 🐈‍."),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Cat")
        verbose_name_plural = _("Cats")

    def __str__(self):
        return self.name
