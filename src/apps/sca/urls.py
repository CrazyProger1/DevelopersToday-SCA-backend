from rest_framework import routers

from src.apps.sca.views import (
    CatViewSet,
    BreedViewSet,
    MissionViewSet,
    TargetViewSet,
    NoteViewSet,
)

router = routers.DefaultRouter()
router.register(
    "api/v1/cats",
    CatViewSet,
    basename="cats",
)
router.register(
    "api/v1/breeds",
    BreedViewSet,
    basename="breeds",
)
router.register(
    "api/v1/missions",
    MissionViewSet,
    basename="missions",
)
router.register(
    "api/v1/targets",
    TargetViewSet,
    basename="targets",
)
router.register(
    "api/v1/notes",
    NoteViewSet,
    basename="notes",
)

urlpatterns = [
    *router.urls,
]
