from src.apps.sca.models import Breed


def create_breed_if_not_exist(name: str):
    Breed.objects.get_or_create(name=name)


def get_all_breeds():
    return Breed.objects.all()
