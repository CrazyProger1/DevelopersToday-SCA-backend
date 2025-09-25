from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.sca.models import Cat
from src.utils.django.admin import ImageTagAdminMixin


@admin.register(Cat, site=site)
class CatAdmin(ImageTagAdminMixin, ModelAdmin ):
    list_display = (
        "image_tag",
        "name",
        "breed",
        "experience",
        "salary",
    )
    list_display_links = (
        "image_tag",
        "name",
    )
    search_fields = (
        "name",
    )
