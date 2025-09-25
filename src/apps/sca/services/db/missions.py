from src.apps.sca.models import Mission, Cat


def get_all_missions():
    return Mission.objects.all()


def is_mission_assigned(mission: Mission):
    return mission.cat is not None


def assign_cat_to_mission(mission: Mission, cat_id: int):
    mission.cat_id = cat_id
    mission.save(update_fields=("cat_id",))


def mark_mission_completed(mission: Mission):
    mission.is_completed = True
    mission.save(update_fields=("is_completed",))
