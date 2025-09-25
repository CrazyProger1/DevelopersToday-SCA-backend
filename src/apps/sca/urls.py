from rest_framework import routers

from src.apps.sca.views import CatViewSet

router = routers.DefaultRouter()
router.register("api/v1/cats", CatViewSet, basename="cats", )

urlpatterns = [
    *router.urls,
]
