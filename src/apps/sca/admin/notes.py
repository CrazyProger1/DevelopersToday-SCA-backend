from django.contrib import admin
from unfold.admin import ModelAdmin

from src.apps.accounts.sites import site
from src.apps.sca.models import Note


@admin.register(Note, site=site)
class NoteAdmin(ModelAdmin):
    list_display = (
        "target",
        "created_at",
    )
    list_display_links = ("target",)
    autocomplete_fields = ("target",)
