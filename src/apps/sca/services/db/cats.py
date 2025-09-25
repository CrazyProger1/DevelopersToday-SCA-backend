from src.apps.sca.models import Cat


def get_all_cats():
    return Cat.objects.all()
