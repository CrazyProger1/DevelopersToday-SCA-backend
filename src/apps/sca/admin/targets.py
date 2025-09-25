from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.sca.models import Target


@admin.register(Target, site=site)
class TargetAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
        "is_completed",
        "created_at",
    )
    list_display_links = (
        "id",
        "name",
    )
    autocomplete_fields = ("mission",)
    search_fields = ("name",)
    list_filter = ("is_completed",)
