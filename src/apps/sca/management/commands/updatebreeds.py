import logging

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from src.apps.sca.services.db import create_breed_if_not_exist

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get(settings.BREEDS_API_URL)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch breeds!"))

        data = response.json()

        for breed in data:
            name = breed["name"]
            create_breed_if_not_exist(
                name=name,
            )
            logger.debug("Breed updated: %s", name)

        self.stdout.write(self.style.SUCCESS("Breeds successfully updated!"))
