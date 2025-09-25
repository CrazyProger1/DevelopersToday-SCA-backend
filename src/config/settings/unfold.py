from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from src.config.settings.base import INSTALLED_APPS, APPLICATION

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    *INSTALLED_APPS,
]

UNFOLD = {
    "SITE_TITLE": APPLICATION,
    "SITE_HEADER": APPLICATION,
    "SITE_URL": "/docs",
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": "dark",
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Accounts"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:accounts_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "devices",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ]}
}
