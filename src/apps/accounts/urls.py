from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from src.apps.accounts.sites import site

urlpatterns = [
    path("admin/", site.urls),
    path("api/v1/tokens/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/tokens/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
