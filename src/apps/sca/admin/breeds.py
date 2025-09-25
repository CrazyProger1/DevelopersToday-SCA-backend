from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.sca.models import Breed


@admin.register(Breed, site=site)
class BreedAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = ("name",)
