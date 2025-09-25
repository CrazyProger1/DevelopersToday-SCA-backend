from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.sca.models import Mission


@admin.register(Mission, site=site)
class MissionAdmin(ModelAdmin):
    list_display = (
        "cat",
        "is_completed",
        "created_at",
    )
    list_display_links = ("cat",)
    autocomplete_fields = ("cat",)
    list_filter = ("is_completed",)
    search_fields = ("cat",)
