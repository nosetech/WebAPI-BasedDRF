from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("health/", include("health_check.urls")),
    path("sampleapp/", include("sampleapp.urls")),
    path("api/", include("user.urls")),
]

if settings.DEBUG:
    urlpatterns = [
        path("admin/", admin.site.urls),
    ] + urlpatterns
