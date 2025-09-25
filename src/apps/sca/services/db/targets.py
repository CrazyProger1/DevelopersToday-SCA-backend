from src.apps.sca.models import Target


def get_all_targets():
    return Target.objects.all()


def mark_target_completed(target: Target):
    target.is_completed = True
    target.save(update_fields=("is_completed",))
