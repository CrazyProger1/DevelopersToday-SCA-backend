from src.apps.sca.models import Note


def can_update_note(note: Note):
    print(note.target.is_completed, note.target.mission.is_completed)
    return not note.target.is_completed and not note.target.mission.is_completed


def get_all_notes():
    return Note.objects.all()
